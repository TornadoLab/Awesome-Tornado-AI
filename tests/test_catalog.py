"""Offline regression checks: no external services or optional packages required."""
from __future__ import annotations
import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from catalog import load, validate, bibtex, bib_escape, safe_url, csv_text, filter_papers, normalized_title, doi_url
from build import outputs, md
from discover_arxiv import parse_feed
from install_into_repo import install, plan

class CatalogTests(unittest.TestCase):
    def setUp(self):self.data=load()
    def test_catalog_valid(self):self.assertEqual(validate(*self.data),[])
    def test_unique_ids(self):self.assertEqual(len(self.data[0]),len({p['id'] for p in self.data[0]}))
    def test_duplicate_detected(self):
        p,c,s,r=copy.deepcopy(self.data);p.append(copy.deepcopy(p[0]));self.assertTrue(any('duplicate' in e for e in validate(p,c,s,r)))
    def test_future_year_rejected(self):
        p,c,s,r=copy.deepcopy(self.data);p[0]['year']=int(s['snapshot_date'][:4])+1;self.assertTrue(any('future' in e for e in validate(p,c,s,r)))
    def test_missing_field_rejected(self):
        p,c,s,r=copy.deepcopy(self.data);del p[0]['sources'];self.assertTrue(any('missing' in e for e in validate(p,c,s,r)))
    def test_unsafe_url_rejected(self):
        p,c,s,r=copy.deepcopy(self.data);p[0]['url']='javascript:alert(1)';self.assertTrue(any('url' in e for e in validate(p,c,s,r)))
    def test_unknown_route_paper_rejected(self):
        p,c,s,r=copy.deepcopy(self.data);r[0]['papers'].append('invented');self.assertTrue(any('unknown route paper' in e for e in validate(p,c,s,r)))
    def test_reproduction_claim_consistency(self):
        p,c,s,r=copy.deepcopy(self.data);p[0]['verification']['reproduced']=True;self.assertTrue(any('reproduction' in e for e in validate(p,c,s,r)))
    def test_safe_url_checks(self):
        self.assertTrue(safe_url('https://doi.org/10.0000/test'))
        for bad in ['http://example.org','javascript:alert(1)','https://user:pass@example.org','https://example.org/a b',None]:self.assertFalse(safe_url(bad))
    def test_bibtex_partial_authors(self):
        p=copy.deepcopy(self.data[0][0]);p['authors_complete']=False
        self.assertIn(' and others',bibtex(p));self.assertIn('Partial author',bibtex(p))
    def test_bibtex_escaping(self):self.assertEqual(bib_escape('A & B_1 {x}'),r'A \& B\_1 \{x\}')
    def test_legacy_doi_link_survives_markdown(self):
        from urllib.parse import unquote
        p=copy.deepcopy(self.data[0][0])
        p['doi']='10.1175/1520-0493(1978)106<0029:TDBPDR>2.0.CO;2'
        target=re.search(r'\[DOI\]\(([^)]+)\)',md(p)).group(1)
        self.assertEqual(target,doi_url(p['doi']))
        self.assertEqual(unquote(target.removeprefix('https://doi.org/')),p['doi'])
        self.assertNotRegex(target,r'[<>()]')
    def test_csv_formula_escape(self):
        p=copy.deepcopy(self.data[0][0]);p['title']='=1+1';self.assertIn("'=1+1",csv_text([p]))
    def test_search_chinese(self):self.assertTrue(filter_papers(self.data[0],query='雷达'))
    def test_search_agentcaster(self):self.assertEqual([p['id'] for p in filter_papers(self.data[0],query='AgentCaster')],['agentcaster2025'])
    def test_scope_is_not_tornado_proof(self):
        transfer=filter_papers(self.data[0],scope='transfer');self.assertTrue(transfer);self.assertTrue(all(p['scope']=='transfer' for p in transfer))
    def test_deterministic_generation(self):self.assertEqual(outputs(),outputs())
    def test_generated_files_current(self):
        for path,text in outputs().items():self.assertEqual((ROOT/path).read_text(encoding='utf-8'),text,path)
    def test_no_unreplaced_template_tokens(self):
        for path in ['README.md','README.zh-CN.md']:self.assertNotRegex((ROOT/path).read_text(encoding='utf-8'),r'\{\{[A-Z_]+\}\}')
    def test_local_markdown_links_and_explicit_anchors(self):
        for file in list(ROOT.glob('*.md'))+list((ROOT/'guides').glob('*.md'))+list((ROOT/'papers').glob('*.md')):
            for link in re.findall(r'\]\(([^\s)]+)\)',file.read_text(encoding='utf-8')):
                if '://' in link or link.startswith('#'):continue
                name,_,anchor=link.partition('#');target=(file.parent/name).resolve()
                self.assertTrue(target.exists(),f'{file.name}: missing {link}')
                if anchor and target.suffix=='.md':self.assertIn(f'id="{anchor}"',target.read_text(encoding='utf-8'),f'{file.name}: missing explicit anchor {link}')
    def test_discovery_fixture_deduplicates_known_arxiv(self):
        raw=(ROOT/'tests/fixtures/arxiv.xml').read_bytes();candidates,total=parse_feed(raw,{'2510.03349'},set())
        self.assertEqual(total,2);self.assertEqual(len(candidates),1);self.assertEqual(candidates[0]['arxiv'],'0000.00000');self.assertEqual(candidates[0]['review_status'],'unreviewed')
    def test_discovery_deduplicates_title(self):
        raw=(ROOT/'tests/fixtures/arxiv.xml').read_bytes();candidates,_=parse_feed(raw,set(),{normalized_title('AgentCaster: Reasoning-Guided Tornado Forecasting')});self.assertEqual(len(candidates),1)
    def test_discovery_rejects_document_types(self):
        with self.assertRaises(ValueError):parse_feed(b'<!DOCTYPE foo><feed/>',set(),set())
    def test_every_category_populated(self):self.assertTrue(all(any(p['category']==c['id'] for p in self.data[0]) for c in self.data[1]))

class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();base=Path(self.temp.name);self.source=base/'source';self.source.mkdir();self.repo=base/'repo';self.repo.mkdir();(self.source/'README.md').write_text('new\n');self.run_git('init')
    def tearDown(self):self.temp.cleanup()
    def run_git(self,*args):return subprocess.run(['git','-C',str(self.repo),*args],check=True,capture_output=True,text=True).stdout.strip()
    def commit(self):
        self.run_git('add','.');self.run_git('-c','user.name=Test','-c','user.email=test@example.invalid','commit','-m','fixture')
    def test_dry_run_never_copies(self):
        changed,conflicts=install(self.source,self.repo);self.assertEqual(changed,1);self.assertEqual(conflicts,0);self.assertFalse((self.repo/'README.md').exists())
    def test_empty_repo_import(self):
        install(self.source,self.repo,apply=True);self.assertEqual((self.repo/'README.md').read_text(),'new\n');self.assertEqual(self.run_git('symbolic-ref','--short','HEAD'),'curation/tornado-observatory')
    def test_dirty_repo_rejected(self):
        (self.repo/'work.txt').write_text('uncommitted')
        with self.assertRaises(ValueError):plan(self.source,self.repo)
    def test_overwrite_requires_explicit_flag(self):
        (self.repo/'README.md').write_text('old\n');self.commit()
        with self.assertRaises(ValueError):install(self.source,self.repo,apply=True)
        self.assertEqual((self.repo/'README.md').read_text(),'old\n')
    def test_explicit_overwrite_preserves_old_commit(self):
        (self.repo/'README.md').write_text('old\n');self.commit();old=self.run_git('rev-parse','HEAD');install(self.source,self.repo,apply=True,overwrite=True)
        self.assertEqual(self.run_git('rev-parse','HEAD'),old);self.assertEqual(self.run_git('show','HEAD:README.md'),'old');self.assertEqual((self.repo/'README.md').read_text(),'new\n')
    def test_symlink_rejected(self):
        try:(self.repo/'README.md').symlink_to(self.source/'README.md')
        except OSError as exc:
            if getattr(exc,'winerror',None)==1314:self.skipTest('Windows account lacks symlink-creation privilege; this case runs in Linux CI')
            raise
        self.commit()
        with self.assertRaises(ValueError):plan(self.source,self.repo)
    def test_nested_directory_rejected(self):
        with self.assertRaises(ValueError):plan(self.repo,self.repo)
    def test_ignored_existing_file_rejected(self):
        (self.repo/'.gitignore').write_text('README.md\n');self.commit();(self.repo/'README.md').write_text('ignored valuable file')
        with self.assertRaises(ValueError):plan(self.source,self.repo)

if __name__=='__main__':unittest.main()

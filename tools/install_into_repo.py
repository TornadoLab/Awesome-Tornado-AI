"""Dry-run-first importer. Creates a review branch; never commits, pushes or deletes."""
from __future__ import annotations
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE=Path(__file__).resolve().parents[1]
EXCLUDE={'.git','__pycache__','.pytest_cache','review','.DS_Store'}

def git(repo: Path,*args: str,check: bool=True) -> str:
    result=subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True,check=False)
    if check and result.returncode:raise ValueError(result.stderr.strip() or 'Git command failed')
    return result.stdout.strip()

def source_files(source: Path) -> list[Path]:
    out=[]
    for p in sorted(source.rglob('*')):
        rel=p.relative_to(source)
        if any(part in EXCLUDE for part in rel.parts) or p.suffix=='.pyc':continue
        if p.is_symlink():raise ValueError(f'Refusing source symlink: {rel}')
        if p.is_file():out.append(rel)
    return out

def plan(source: Path,repo: Path) -> tuple[list[Path],list[Path]]:
    if source==repo or source in repo.parents or repo in source.parents:
        raise ValueError('Source and destination must be separate, non-nested directories')
    if Path(git(repo,'rev-parse','--show-toplevel')).resolve() != repo.resolve():
        raise ValueError('Destination must be the repository root')
    if git(repo,'status','--porcelain','--untracked-files=all'):
        raise ValueError('Destination has uncommitted/untracked files. Commit or stash them yourself first; nothing was changed.')
    changed=[];conflicts=[]
    for rel in source_files(source):
        target=repo/rel
        for item in [target,*target.parents]:
            if item==repo:break
            if item.is_symlink():raise ValueError(f'Refusing destination symlink: {item}')
        if target.exists() and not target.is_file():raise ValueError(f'Target is not a file: {rel}')
        for parent in target.parents:
            if parent==repo:break
            if parent.exists() and not parent.is_dir():raise ValueError(f'File blocks directory: {parent}')
        if not target.exists() or target.read_bytes()!=(source/rel).read_bytes():
            changed.append(rel)
            if target.exists():
                # Even explicit overwrite may not replace ignored/untracked data.
                tracked=subprocess.run(['git','-C',str(repo),'ls-files','--error-unmatch','--',str(rel)],capture_output=True).returncode==0
                if not tracked:raise ValueError(f'Refusing untracked/ignored existing file: {rel}')
                conflicts.append(rel)
    return changed,conflicts

def install(source: Path,repo: Path,apply: bool=False,overwrite: bool=False,branch: str='curation/tornado-observatory') -> tuple[int,int]:
    source=source.resolve();repo=repo.resolve()
    changed,conflicts=plan(source,repo)
    for rel in changed:print(('REPLACE ' if rel in conflicts else 'ADD     ')+str(rel))
    print(f'{len(changed)} changes; {len(conflicts)} existing-file conflicts. {"APPLY requested" if apply else "DRY RUN — no writes"}.')
    if not apply:return len(changed),len(conflicts)
    if conflicts and not overwrite:raise ValueError('Existing tracked files would be replaced. Review the dry-run list; use --overwrite only after explicitly choosing replacement.')
    if not changed:return 0,0
    subprocess.run(['git','check-ref-format','--branch',branch],check=True,capture_output=True,text=True)
    # -b refuses an existing branch. Also works on an unborn repository with no first commit.
    git(repo,'checkout','-b',branch)
    for rel in changed:
        target=repo/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source/rel,target)
    print(f'Files copied on {branch}. No commit or push performed. Review git diff and git status before publishing.')
    return len(changed),len(conflicts)

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--apply',action='store_true')
    ap.add_argument('--overwrite',action='store_true',help='Explicitly replace conflicting TRACKED files; preserve original commits on the original branch')
    ap.add_argument('--branch',default='curation/tornado-observatory')
    args=ap.parse_args()
    try:install(SOURCE,args.repo,args.apply,args.overwrite,args.branch);return 0
    except (ValueError,OSError,subprocess.SubprocessError) as exc:
        print(f'Import stopped: {exc}',file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())

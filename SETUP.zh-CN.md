# 导入、预览与发布

## 仓库与网页

仓库地址为 [TornadoLab/Awesome-Tornado-AI](https://github.com/TornadoLab/Awesome-Tornado-AI)。维护源在 `data/` 和 `templates/`，生成后的静态网页在 `docs/`。获取私有仓库需要相应的 GitHub 权限；仓库推送和 GitHub Pages 发布是两个独立步骤。

本轮已核实 derong 对应的 GitHub SSH 身份为 `DerongDeng-dero`。Pages 未启用；可先使用下面的本地预览。只有需要把这份模板导入另一个已有仓库时，才使用 B、C 节。

## A. 先看成品

克隆或解压后进入 `Awesome-Tornado-AI` 文件夹。Python 3.10+ 即可运行核心脚本，网页无需安装依赖：

```bash
python -m http.server 8000 --directory docs
```

浏览器打开 `http://localhost:8000`。也可直接打开 `docs/index.html`；浏览器对本地文件的剪贴板或存储限制不会阻断检索，BibTeX 复制失败时会回退到文件导出。

## B. 可选：导入另一个已有仓库

让解压的模板目录与 git 克隆目录并列放置，避免把模板复制到其自身。以下命令从两个目录共同的父目录执行：

```bash
git clone git@github.com:TornadoLab/Awesome-Tornado-AI.git Awesome-Tornado-AI-remote
python Awesome-Tornado-AI/tools/install_into_repo.py --repo Awesome-Tornado-AI-remote
```

上述 Python 命令只列出拟添加和拟替换文件，**不写入任何文件**。它要求目标仓库工作区干净；拒绝符号链接、嵌套目录、非仓库根目录以及覆盖未被 git 跟踪的现有文件。

确认清单没有冲突后：

```bash
python Awesome-Tornado-AI/tools/install_into_repo.py --repo Awesome-Tornado-AI-remote --apply
```

如果存在已跟踪文件冲突，脚本会停止。只在逐项检查后明确决定替换时使用：

```bash
python Awesome-Tornado-AI/tools/install_into_repo.py --repo Awesome-Tornado-AI-remote --apply --overwrite
```

`--apply` 会新建并切换到 `curation/tornado-observatory` 分支，然后复制文件。不会删除额外文件，不会 commit、push 或修改远端，也不会更改全局 git 配置。原有提交保留在原分支中。若分支名已存在，可指定 `--branch curation/tornado-observatory-v2`。

**特别检查许可证和现有文献。** 模板的 LICENSE 不应未经确认替换原仓库的授权意图；已有论文记录应在 canonical JSON 中合并去重。导入不是自动语义合并器。复制中断时不要运行破坏性清理命令；用 `git status` 检查当前分支的局部修改，再人工恢复或继续。

## C. 检查后提交

```bash
cd Awesome-Tornado-AI-remote
python tools/validate.py
python tools/build.py --check
python -m unittest discover -s tests -v
git status --short
git diff --stat
git diff
# 新增文件也要查看；git diff 默认不会展示未跟踪文件的内容。
```

确认文件和许可后，再主动执行：

```bash
git add README.md README.zh-CN.md RESOURCES.md CONTRIBUTING.md SETUP.zh-CN.md \
  LICENSE CITATION.cff CHANGELOG.md CODE_OF_CONDUCT.md .gitignore .gitattributes \
  .github assets data docs guides licenses papers templates tests tools
git commit -m "Build tornado research observatory and source-linked paper atlas"
git push -u origin curation/tornado-observatory
```

上面的多行命令使用 POSIX shell 换行写法。PowerShell 用户可把 `git add` 写成一行；不要照搬反斜杠换行。推送后再创建 PR，审阅并合并到你实际使用的默认分支。不要 force-push。

## D. 发布 GitHub Pages

本站是静态站点，所有发布文件已经在 `docs/`。按 [GitHub 官方发布源说明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) 选择 **Deploy from a branch**，使用实际存在且已合并这些文件的分支和 `/docs` 目录，然后保存。

如果组织设置、仓库可见性或套餐限制 Pages，请遵循该仓库的配置要求；这些权限在本交付中未验证。`docs/.nojekyll` 已包含。不要把本地文件的存在误写为已经部署成功。成功部署且未配置自定义域名时，项目站点通常形如：

```text
https://tornadolab.github.io/Awesome-Tornado-AI/
```

实际可访问后，再把这个地址加入 README 的顶部导航和仓库 About 的 Website。当前模板不放一个未经验证的“在线成功”徽章。

## E. 更新文献

在 `data/papers.json` 添加/修改条目，必要时更新 `data/config.json` 的快照日期。`data/categories.json` 管理主题，`data/routes.json` 管理阅读路线。README 的手工文字在 `templates/`，而不是生成后的根目录副本。

```bash
python tools/validate.py
python tools/build.py
python tools/build.py --check
```

## F. 可选的新论文发现

```bash
python tools/discover_arxiv.py --since 2026-09-01 --until 2026-09-29 --max-results 100
```

输出在 `review/candidates.json`，默认被 git 忽略。这个队列不是正式收录；需要人工审核。它只检索 arXiv 的一部分候选，不会覆盖 AMS、IEEE、中文期刊等全部来源。截断时缩小日期区间再检索。

GitHub Actions 中也有 **Scout new arXiv candidates (manual)**。默认只能手动运行，无计划任务，也不会自动发 issue、提交或修改正式目录。需要固定周期时，再明确决定是否启用示例 cron，并安排审稿人。公开 API 连通性、实际 GitHub CI 和 Pages 部署仍需在有网络和仓库权限的环境中验证。

## G. 推荐的仓库 About 文案

```text
A source-linked atlas of tornado research: physics, radar detection, intensity, prediction, deep learning and multimodal reasoning.
```

推荐 topics（需仓库管理员自行设置）：

```text
tornado meteorology severe-weather weather-radar tornado-detection
weather-forecasting deep-learning multimodal-learning awesome-list ai4science
```

## H. 本次验证边界

见 [交付检查报告](guides/QUALITY_REPORT.md)：31 项离线测试、21 项浏览器检查已通过；浏览器测试使用内存中的单文件页面。当前容器阻止本地页面导航，因此没有把它算作 HTTP / GitHub Pages 部署验证；实际跨刷新本地存储与外部 API 连通性仍需在目标环境检查。

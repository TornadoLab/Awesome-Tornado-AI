<p align="center"><img src="assets/banner.svg" alt="Awesome Tornado AI：从第一束雷达回波，到下一代龙卷智能。" width="100%"></p>

<h1 align="center">🌪 Awesome Tornado AI</h1>
<p align="center"><strong>一张持续生长的龙卷研究地图：理解、识别、检测、分级、预测与推理。</strong><br>物理机制 → 雷达证据 → 传统统计 → 深度学习 → 多模态智能体</p>
<p align="center"><a href="{{WEBSITE_URL}}">在线网站</a> · <a href="README.md">English</a> · <a href="papers/README.md">论文地图</a> · <a href="guides/READING_ROUTES.md">阅读路线</a> · <a href="RESOURCES.md">数据与工具</a> · <a href="SETUP.zh-CN.md">部署说明</a></p>

> **已收录 {{COUNT}} 条文献 · {{CATEGORY_COUNT}} 个研究方向 · {{START_YEAR}}—{{END_YEAR}} · 检索快照 {{DATE}}**
>
> **{{ANNOTATED_COUNT}} 条已有方法注释，{{BIBLIOGRAPHIC_COUNT}} 条为待深入阅读的书目记录，{{CODE_COUNT}} 条附已核实的代码链接。** 龙卷直接相关 {{DIRECT_COUNT}} 条、强对流与业务背景 {{CONTEXT_COUNT}} 条、可迁移天气 AI {{TRANSFER_COUNT}} 条。检索范围广，但**尚未穷尽全领域**；元数据核验不等于全文精读或独立复现。

## 不只是一个很长的 README

**阅读论文：** [完整目录](papers/ALL_PAPERS.md) · [论文与 GitHub／代码索引](papers/CODE_INDEX.md) · [分主题浏览](papers/README.md) · [BibTeX](papers/references.bib) · [CSV](papers/catalog.csv)。

**探索网页：** [在线访问研究地图]({{WEBSITE_URL}})。也可本地打开 `docs/index.html`，或运行：

```bash
python -m http.server 8000 --directory docs
# 浏览器打开 http://localhost:8000
```

网页带有中英文关键词搜索、研究方向/年份/研究范围/发表状态/代码筛选、随机追论文、三条阅读路线、浏览器本地阅读清单及筛选结果 BibTeX 导出。不需要 npm、服务器数据库或 API key。配色与矢量图围绕雷达、涡旋和科研观测站设计；图案是装饰性原创图，不冒充实测雷达图。

网站已通过 **GitHub Pages 上线**，启用 HTTPS，并从 `main` 分支的 `docs/` 目录发布。更新和本地预览步骤见 [SETUP.zh-CN.md](SETUP.zh-CN.md)。

龙卷图加入了旋转流线、漏斗摆动和尘粒动画，支持暂停、系统“减少动态效果”设置及离屏暂停。README 的 SVG 横幅也包含动画；不支持 SVG 动画的阅读器仍能显示静态图。

**相对最初的 67 条，本轮增加 {{ADDED_COUNT}} 条。** 已完成 36 组 Crossref 检索中的 33 组、期刊与机构原始页面检索，以及一次 2026 年 arXiv 实时检索。方法注释与书目索引分别标记；检索上限、排除项、待核验候选和版本合并见 [搜集记录](guides/COLLECTION_LOG.md)。

## 先按问题分，再按方法找

| # | 研究方向 | 条目 |
|---|---|---:|
{{CATEGORY_TABLE_ZH}}

网站也为每篇文献显示研究方法、输入、目标与预测时间窗。传统研究不是 AI 的陪衬：TVS、TDS、环境判据、EF 分级、人工警报验证，都决定了一个机器学习实验究竟在解决什么。

## 三种研究范围，不能混为一谈

**Direct**：直接研究龙卷的物理、检测、发生预测、等级或灾损。**Context**：强对流、区域模式、预报员工作流等直接背景。**Transfer**：可能迁移到龙卷研究的通用天气 AI，但不能因此声称已经在龙卷任务上有效。

例如，[TorNet](papers/data.md#tornet2025) 是 MIT Lincoln Laboratory 的雷达数据集；[AgentCaster](papers/agents.md#agentcaster2025) 研究的是带气象背景的区域龙卷预报；[RadarQA](papers/agents.md#radarqa2025) 评估雷达预报质量；[2026 年的概率反射率临近预报研究](papers/forecast.md#erickson2026)预测龙卷风暴中的雷达回波演变。它们都值得收录，但不是同一个标签、尺度与时间窗上的模型竞赛。

从 [1953 年钩状回波观测](papers/radar.md#stout1953)、[1970 年多普勒涡旋识别](papers/radar.md#donaldson1970)、[1971 年藤田原始报告](papers/rating.md#fujita1971)、[1978 年脉冲多普勒检测](papers/radar.md#brown1978)、[1996 年神经网络预测](papers/ml.md#marzban1996)，到 [三维多尺度深度学习](papers/dl.md#lagerquist2020)、[TPA](papers/ml.md#sandmael2023)、[TorDet](papers/dl.md#tordet2025)、[跨国雷达泛化评估](papers/evaluation.md#jiang2026) 和 [AgentCaster](papers/agents.md#agentcaster2025)，可以沿着方法谱系阅读，也可以从 [三条学习路线](guides/READING_ROUTES.md) 开始。

物理与传统方法还包括 [实验室涡旋](papers/foundations.md#ward1972)、[非超级单体龙卷模拟](papers/foundations.md#lee1997b)、[中国龙卷雷达同化](papers/forecast.md#chen2019funing)、[强度分级制度](papers/rating.md#doswell2009) 和 [预警长期检验](papers/evaluation.md#brooks2018)。近期智能方法包含 [ASTRA](papers/impacts.md#umeike2026)、[TornadoNet](papers/impacts.md#tornadonet2026) 与 [视觉语言灾损解释](papers/agents.md#shakya2026)；灾后损伤识别与龙卷发生预测分别标注。

## 学术底线

[任务与评测指南](guides/TASKS.md) 专门处理容易混淆的地方：当前检测不等于未来发生预测；灾损等级不等于直接测得的风速；六种雷达变量不自动等于六个传感模态；区域天气模拟能力不等于龙卷事件级预报能力；缺少开放代码链接不代表代码不存在。

每条数据带来源、检查日期和核验级别。本轮补齐了原目录中 17 条作者名单；新增书目采用出版方存入的作者信息，身份尚不完整的条目明确标记。正式投稿时仍需核对引用格式及后续更正。对 [Wurman 等人的强度研究](papers/rating.md#wurman2021) 保留了 2025 年更正来源；已识别出的同一工作版本合并计数。

## 持续扩充，而不是越积越乱

只维护 `data/papers.json`，然后自动生成网页数据、双语入口、主题目录、BibTeX 和 CSV：

```bash
python tools/validate.py
python tools/build.py
python tools/build.py --check
python -m unittest discover -s tests -v
```

新论文建议遵循 [贡献规范](CONTRIBUTING.md)。可选的 arXiv 发现脚本只生成“待人工审核队列”；不会自动把搜索结果当作可靠论文收入正式库，也没有默认开启定时任务。

早期观测、中文个例、非超级单体/水龙卷、数值模拟、风工程、卫星/闪电/次声、预警检验与社会影响均已扩充。接下来需要补足中文数据库、书籍和学位论文的检索，逐条完善书目记录的方法注释，并继续追查遗漏与版本关系；详见 [覆盖缺口与扩展路线](guides/RESEARCH_GAPS.md)。

## 致谢与授权

参考 [Awesome WeatherAI](https://github.com/HeQinWill/awesome-WeatherAI) 的领域资源组织、[Awesome AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) 的天气与气候研究分类、[Awesome 3D Gaussian Splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) 的可检索论文库设计，以及 [Awesome](https://github.com/sindresorhus/awesome) 的策展规范。没有复制它们的视觉素材或代码。

代码、网页与原创矢量素材采用 MIT；原创文字注释采用 CC BY 4.0。论文、数据集及第三方商标遵循原有权利和许可，见 [LICENSE](LICENSE)。引用索引本身可用 [CITATION.cff](CITATION.cff)，引用研究结论仍应引用原论文。

**用于研究检索与交流，不提供业务预警，也不应据此做紧急避险决策。**

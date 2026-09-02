# my-skills 触发速查表 / SKILLS INDEX

> 来源：github.com/Artistsj/my-skills（main · .agents/skills/）· 共 **41 个技能 / 9 大类**
> 用法：在 AI 助手中说"用 XX skill 来做"，或直接说出下面的触发关键词，助手会匹配对应技能并按其框架执行。
> 标记：★ = 核心旗舰技能；💤 = 已被同系列覆盖、策略中标注休眠（保留但不主动触发）。

---

## 快速反查索引（按你想做的事找 skill）

| 你想做的事 | 用哪个 skill |
|---|---|
| 做网页演示 / 路演 / 动画幻灯片 | `frontend-slides` |
| 生成可编辑的 .pptx 文件 | `ppt-generation` |
| 写 / 读 / 改 Word 文档 | `docx` |
| 设计界面、选色板字体、做设计系统 | `ui-ux-pro-max` ★ |
| 定视觉方向 / 美学方法论 | `frontend-design` |
| 审查 UI 代码是否符合规范 | `web-design-guidelines` |
| 无障碍 / WCAG / 键盘对比度检查 | `accessibility` |
| 扮演挑剔用户挑 UX 毛病 | `adversarial-ux-test` |
| 快速做个原型验证想法 | `prototype` |
| React / Next.js 性能优化 | `vercel-react-best-practices` |
| 画专业架构图 / 流程图 / Excalidraw | `diagram-maker` |
| 对话里快速画个草图解释概念 | `show-me` |
| 动手写代码前先理需求 | `brainstorming` |
| 设计模块接口 / 深模块 | `codebase-design` |
| 扫描代码库找架构问题 | `improve-codebase-architecture` |
| 排查疑难 bug / 性能问题 | `diagnosing-bugs` |
| 测试驱动开发 TDD | `tdd` |
| 梳理领域模型 / 写 ADR | `domain-modeling` |
| 把当前对话打包交接给别人 | `handoff` |
| 优化 CLAUDE.md 指令 | `improve-claude-md` |
| 拷问 / 压力测试一个方案（产出 ADR） | `grill-with-docs` |
| A股收盘复盘 / 市场日报 | `market-daily-review` |
| A股个股尽调 / 体检 / 基本面报告 | `a-share-stock-dossier` |
| 期货研判 / 主力合约 / 跨期套利 | `futures-deepview-analyst` |
| 做融资 BP / 一页纸 / 财务模型 | `investor-materials` |
| 风险评估 / 风险登记册 | `risk-assessment` |
| 档案管理系统规划 / 收管存用 | `archives-lifecycle` |
| 业务系统对接档案 / 自动归档 | `archives-yidang-yiti` |
| 预归档 / 兼职档案员 / 收集前置 | `archives-pre-archiving` |
| 档案权限 / 分级分权 / 全宗 | `archives-permissions` |
| 档案借阅 / 水印 / 原文遮盖 | `archives-access-control` |
| 电子档案四性检测 / 合规 | `archives-four-tests` |
| 双套制转单套制 / 数字化转型 | `archives-dual-to-single` |
| 把一本书 / 视频 / 课程蒸馏成技能 | `cangjie-skill` |
| 算命 / 八字 / 紫微斗数 / 排盘 | `fortune` |
| 格式化天气播报 | `weather-reporter` |
| 给 issue / PR 做分诊 | `triage` |
| 找有没有能做 X 的技能 | `find-skills` |
| 创建 / 修改 / 评测一个技能 | `skill-creator` |

---

## ① 研发流程与架构（8）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `brainstorming` | 做新功能/组件/改行为之前、"先想想"、需求发想、creative work 前置 | 任何创造性工作前强制探明用户意图、需求与设计 |
| `codebase-design` | 设计模块接口、深模块、seam 在哪、可测试性、AI 可导航 | "深模块"设计共享词汇与接口边界原则 |
| `improve-codebase-architecture` | 扫描架构、改进架构、找浅模块、架构重构、deepening opportunities | 扫描代码库找架构改进点，输出可视化 HTML 报告并引导拷问 |
| `diagnosing-bugs` | diagnose / debug this、报错、崩了、失败、慢、性能回归 | 疑难 bug 与性能回归的系统化诊断循环 |
| `tdd` | red-green-refactor、测试先行、集成测试、test-first | 测试驱动开发循环 |
| `domain-modeling` | 领域模型、CONTEXT.md、ADR、术语表、ubiquitous language | 构建并打磨项目领域模型，维护 CONTEXT.md 与 ADR |
| `handoff` | 交接、换设备继续、压缩对话、交接文档、pick up where I left | 把当前对话压缩成交接文档供另一个 agent 接手 |
| `improve-claude-md` | 优化 CLAUDE.md、指令遵循、important if 块 | 用 `<important if>` 块改进 CLAUDE.md，提升指令遵循度 |

## ② UI/UX 与前端（7）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `ui-ux-pro-max` ★ | 设计/构建/审查/修复界面、页面、组件、设计系统、选色板/字体/图标、响应式、accessibility、charts | 旗舰设计智能库：79 风格 / 192 色板 / 74 字体 / 119 UX 规则 / 25 图表 / 22 技术栈 |
| `frontend-design` | 设计方向、美学指导、视觉方向、避免模板化、distinctive visual design | 定视觉方向与美学方法论，让设计有意图不模板化 |
| `web-design-guidelines` | review my UI、check accessibility、audit design、review UX、检查网站最佳实践 | 按 Web 界面规范审查 UI 代码（布局/交互/响应式） |
| `accessibility` | WCAG 2.2、无障碍、键盘导航、对比度、读屏、screen reader、ARIA | 按 WCAG 2.2 AA 做无障碍设计、实现与审计 |
| `adversarial-ux-test` | UX 痛点、压力测试、扮演用户挑刺、恶意用户、hostile user roleplay | 扮演"恶意/挑剔用户"压力测试流程，发现并分级 UX 痛点 |
| `prototype` | 快速原型、验证设计、sanity-check、状态模型、throwaway prototype | 构建一次性原型，快速验证状态模型、逻辑或界面方向 |
| `vercel-react-best-practices` | React / Next.js 性能、bundle 优化、数据获取、组件优化、refactor React | Vercel 工程团队的 React/Next.js 性能优化最佳实践 |

## ③ 档案管理（7，中文自建 · 源自《泛微文书定》拆书）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `archives-lifecycle` | 收管存用、档案全生命周期、档案管理流程、档案系统功能规划 | 档案"收管存用"全生命周期总框架（总纲） |
| `archives-yidang-yiti` | 业档一体、业档融合、业务档案一体化、自动归档、档案系统对接 | 业务系统与档案系统深度融合、电子文件自动归档与反向调用 |
| `archives-pre-archiving` | 预归档、收集前置化、兼职档案员、单兵作战、档案预整理 | 预归档：收集整理前置化、业务/兼职/专职三级协作 |
| `archives-permissions` | 分级分权、全宗、档案权限、按岗授权、多组织权限、档案门限权限 | 集团型多全宗档案的分级分权权限体系（五维控制） |
| `archives-access-control` | 原文遮盖、动态水印、档案借阅、利用控制、档案安全利用、借阅副本 | 档案利用控制：检索/借阅/操作/内容四层控制，动态水印、原文遮盖 |
| `archives-four-tests` | 四性检测、真实性、完整性、安全性、可用性、电子档案合规、DA/T70 | 电子档案"四性检测"（真实/完整/安全/可用），三节点把关 |
| `archives-dual-to-single` | 双套制、单套制、电子档案单套管理、纸质数字化、档案数字化转型 | 从纸质+电子双套制渐进过渡到电子单套制的路径 |

## ④ 金融投研与商业（5，中文自建 · 数据走 Pandadata）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `market-daily-review` | A股收盘复盘、市场日报、收盘总结、龙虎榜、北向资金、涨跌停情绪 | A股收盘复盘：指数/估值/宽度/情绪/行业/龙虎榜/北向等 |
| `a-share-stock-dossier` | A股个股体检、个股尽调、公司全面分析、股票基本面报告、质押解禁减持风险排查 | A股个股尽调：概况/财务/分红/股东行为/质押解禁减持/资金面 |
| `futures-deepview-analyst` | 期货、主力合约、跨期结构、席位持仓、多空比、基差、期限结构、库存、套利 | 期货品种/主力合约/跨期结构综合研判（Pandadata DeepView） |
| `investor-materials` | pitch deck、一页纸、投资人备忘录、加速器申请、财务模型、融资材料、use of funds | 制作并保持一致的融资 BP、一页纸、备忘录、财务模型 |
| `risk-assessment` | what are the risks、risk assessment、risk register、what could go wrong、风险评估 | 识别、评估并缓解运营风险，输出风险登记册与应对措施 |

## ⑤ 学习 / 生活 / 协作（4）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `cangjie-skill` | 拆书、蒸馏一本书、把 XX 书做成 skill、把视频/播客/课程蒸馏成 skill、turn a book into skills | 把书/长视频/播客/课程/访谈提炼为原子化、可调用的技能集 |
| `fortune` | 算命、算八字、看八字、批八字、排盘、紫微、紫微斗数、帮我看看命、我的运势、今年运势、合婚、bazi、ziwei | 交互式收集出生信息，调用排盘脚本做八字+紫微斗数分析 |
| `weather-reporter` | 天气、格式化天气、温度区间、活动建议 | 用表情、温度区间与活动建议格式化天气信息 |
| `triage` | issue 分诊、PR 分诊、triage、分类 issue、外部 PR 处理 | 让 issue 与外部 PR 走分诊角色状态机，产出 agent 可用简报 |

## ⑥ 演示与文档（3）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `frontend-slides` | 做演示、做 slides、presentation、PPT 转网页、演讲幻灯片、路演、产品发布 | 从零或由 PPT 生成动画丰富的 HTML 网页演示，跨平台免 Office |
| `ppt-generation` | 做 PPT 文件、生成 PPTX、PowerPoint、可编辑幻灯片 | 逐页生成图片并合成为原生可编辑 .pptx 文件 |
| `docx` | Word doc、word document、.docx、.dotx、报告、备忘录、信件、模板、目录页码 | Word(.docx/.dotx) 的创建、读取、编辑、套模板、修订与目录 |

## ⑦ 思辨拷问（3）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `grill-with-docs` | 拷问我、stress-test、拷问方案、产出 ADR、relentless interview | 不留情面地拷问计划/设计，并同步产出 ADR 与术语表（**统一主入口**） |
| `grill-me` 💤 | 拷问（轻量入口） | 拷问流程入口，功能已被 grill-with-docs 覆盖，休眠 |
| `grilling` 💤 | 拷问（纯逻辑） | 纯拷问逻辑内核，作为 grill-with-docs 内部依赖，休眠 |

## ⑧ 可视化与图解（2）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `diagram-maker` | 画流程图、画架构图、Excalidraw、SVG 图、白板、concept diagram | 生成专业 SVG/HTML 或 Excalidraw 的概念图、架构图、流程图 |
| `show-me` | 给我看看、解释一下、看不懂、快速草图、Mermaid、code-shape sketch | 对话中用精简图示、代码草图、Mermaid、小 HTML 快速解释当前话题 |

## ⑨ 技能元管理（2）

| 技能 | 触发关键词 / 场景 | 一句话功能 |
|---|---|---|
| `find-skills` | how do I do X、find a skill for X、is there a skill、找技能、装技能、discover skills | 当用户问"有没有能做 X 的技能"时，帮助发现并安装技能 |
| `skill-creator` | 创建 skill、修改 skill、优化 skill、评测 skill、触发准确率、benchmark、evals | 创建、修改、优化技能，并通过评测/方差分析衡量触发准确率与表现 |

---

## 6 条常用协作流水线（来自 SKILL-STRATEGY.md）

1. **从零做产品演示**：`brainstorming` → `frontend-design` → `ui-ux-pro-max` → `frontend-slides` → `handoff`
2. **审查并改进 Web 页面**：`web-design-guidelines` → `accessibility` → `adversarial-ux-test` → `prototype`
3. **架构重构**：`improve-codebase-architecture` → `codebase-design` → `grill-with-docs` → `tdd`
4. **A股投研全流程**：`market-daily-review` → `a-share-stock-dossier` → `futures-deepview-analyst`
5. **Bug 修复**：`diagnosing-bugs` → `prototype` → `tdd`
6. **创建新 Skill**：`find-skills` → `skill-creator` → `improve-claude-md`

---

## 边界说明

- **纯方法论/流程类**（档案系列、grill、brainstorming、tdd、handoff、skill-creator、frontend-design、web-design-guidelines、accessibility 等）：AI 助手可以在对话中直接按其框架执行。
- **依赖本地脚本或外部接口**（`ui-ux-pro-max` 的 search.py、`fortune` 排盘脚本、金融 3 连的 Pandadata 接口、`docx`/`ppt-generation` 的文档生成库）：需要在本地 AI 助手环境（Claude Code / Cursor 等）里用 `uipro init --ai <平台>` 安装后才能真正跑脚本；对话中可以给出思路和框架，但不假装执行了原脚本。
- 说"按 skill 来"或"用 XX skill"，助手会先在这 41 个里匹配再动手。

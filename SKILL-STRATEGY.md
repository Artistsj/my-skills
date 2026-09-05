# Skill 使用策略

> 基于 **42 个 skill** 的冲突分析，制定明确的使用优先级和触发规则。
> 完整技能清单与触发词速查见 [SKILLS-INDEX.md](./SKILLS-INDEX.md)。

---

## 一、冲突解决策略：每组冲突选定"主 Skill"

### 冲突 1：演示文稿 — frontend-slides vs ppt-generation

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 需要可编辑的 .pptx 文件 | ppt-generation | 输出原生 PowerPoint，可在 Office/WPS 编辑 |
| 需要网页演示、动画丰富 | frontend-slides | HTML 格式，跨平台、动画强、无需 Office |
| 产品发布会、路演 | frontend-slides | 视觉冲击力强，支持动画和交互 |
| 内部汇报、需他人编辑 | ppt-generation | 兼容性好，可协作编辑 |

**规则**：默认用 frontend-slides（视觉效果更好），只在明确需要 .pptx 文件格式时用 ppt-generation。

---

### 冲突 2：UI 设计指导 — frontend-design vs ui-ux-pro-max

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 需要设计方向、美学方法论 | frontend-design | 提供设计思维指导，避免模板化 |
| 需要具体色板、字体、图标选择 | ui-ux-pro-max | 数据驱动，79 风格、192 色板、74 字体 |
| 新项目从零设计 | 两者配合 | 先 design 定方向，再 pro-max 选具体数据 |
| 已有设计稿，需要落地实现 | ui-ux-pro-max | 提供技术栈适配和组件库参考 |

**规则**：两者不是竞争而是配合。frontend-design 是"大脑"（定方向），ui-ux-pro-max 是"工具箱"（选数据）。新项目先 design 后 pro-max，已有方向直接 pro-max。

---

### 冲突 3：拷问系列 — grill-me vs grilling vs grill-with-docs

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 任何拷问场景 | grill-with-docs | 功能最全，整合 grilling + domain-modeling |
| 只想快速拷问，不需要文档 | grilling | 轻量，纯拷问逻辑 |
| 不需要 | grill-me | 它只是入口，直接用 grill-with-docs 替代 |

**规则**：统一用 grill-with-docs 作为唯一入口。grilling 和 grill-me 作为内部依赖被自动调用，不需要手动触发。等效于"删除" grill-me 和 grilling 的独立触发。

---

### 冲突 4：可视化 — show-me vs diagram-maker

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 对话中快速解释概念 | show-me | 轻量，代码草图、Mermaid、diff |
| 需要专业 SVG/HTML 图表 | diagram-maker | 支持 Excalidraw、复杂架构图 |
| "给我看看" / "看不懂" | show-me | 自动触发，解释当前话题 |
| "画个流程图" / "画架构图" | diagram-maker | 专业制图，可导出 |

**规则**：对话解释用 show-me，专业制图用 diagram-maker。看触发词：解释性请求 → show-me，制图性请求 → diagram-maker。

---

### 冲突 5：Web 审查 — web-design-guidelines vs accessibility

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 全面 UI 审查 | web-design-guidelines | 覆盖布局、交互、响应式、最佳实践 |
| 专项无障碍合规检查 | accessibility | 专注 WCAG 2.2 Level AA，生成 ARIA |
| 新项目设计阶段 | 两者配合 | 先 guidelines 审整体，再 accessibility 补无障碍 |
| 已有页面合规修复 | accessibility | 针对性修复无障碍问题 |

**规则**：先 web-design-guidelines 做全面审查，再 accessibility 做无障碍专项。两者是"先全面后专项"的配合关系。

---

### 冲突 6：架构改进 — codebase-design vs improve-codebase-architecture

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 想知道设计原则和理论 | codebase-design | 查阅深模块设计原则、接口边界 |
| 想主动扫描架构问题 | improve-codebase-architecture | 生成 HTML 报告，找出浅模块 |
| 架构重构项目 | 两者配合 | 先 improve 扫描找问题，再 design 查原则指导修改 |

**规则**：先 improve-codebase-architecture 扫描（主动发现问题），再 codebase-design 查阅（指导修改方向）。improve 是"诊断"，design 是"处方"。

---

### 冲突 7：档案管理系列内部配合 — 7 个 archives-* skill 的分工

档案系列 7 个技能不是竞争关系，而是**按档案管理阶段和维度分工**的配合体系：

| 阶段/维度 | 使用 Skill | 触发场景 |
|---|---|---|
| 总纲 / 全流程规划 | `archives-lifecycle` | 做档案系统整体规划、梳理收管存用流程 |
| 业务系统对接 / 自动归档 | `archives-yidang-yiti` | 业务系统与档案系统打通、电子文件自动归档 |
| 收集前置 / 预归档 | `archives-pre-archiving` | 兼职档案员、收集整理前置、预归档流程 |
| 权限体系 / 分级分权 | `archives-permissions` | 多全宗、按岗授权、门限权限、权限模型设计 |
| 利用控制 / 安全借阅 | `archives-access-control` | 档案借阅审批、动态水印、原文遮盖、利用审计 |
| 合规检测 / 四性检测 | `archives-four-tests` | 电子档案真实性/完整性/安全性/可用性检测、DA/T70 合规 |
| 数字化转型 / 双套转单套 | `archives-dual-to-single` | 从纸质+电子双套制过渡到电子单套制的路径规划 |

**规则**：
- 做**整体规划**时先 `archives-lifecycle`（总纲），再按需深入具体阶段。
- 做**系统建设**时按流水线：`archives-yidang-yiti`（对接）→ `archives-pre-archiving`（收集）→ `archives-permissions`（权限）→ `archives-access-control`（利用）→ `archives-four-tests`（合规）。
- `archives-dual-to-single` 是**转型战略**，独立于日常运营，在数字化转型项目中单独使用。

---

### 冲突 8：技能创建 — cangjie-skill vs skill-creator vs find-skills

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 从书/视频/课程中蒸馏技能 | `cangjie-skill` | 专门处理长内容的原子化蒸馏，产出可调用技能集 |
| 从零创建/修改/评测一个技能 | `skill-creator` | 通用技能创建、优化、评测（evals/方差分析） |
| 先看看有没有现成技能 | `find-skills` | 避免重复造轮子，先搜索再决定是否创建 |

**规则**：创建新技能的标准流水线是 `find-skills`（先查有没有）→ 如果原料是书/课程用 `cangjie-skill`（蒸馏）→ 用 `skill-creator`（创建/优化/评测）。三者是"先查 → 再蒸馏 → 后创建"的配合关系。

---

### 冲突 9：文档写作格式 — obsidian-markdown vs docx

| 场景 | 使用 Skill | 原因 |
|---|---|---|
| 在 Obsidian 库内新建/改写 .md 笔记 | obsidian-markdown | 输出 wikilink、callout、frontmatter、embed 等 Obsidian 风味语法 |
| 处理双链 `[[]]`、标注 `> [!]`、Properties | obsidian-markdown | 这是 Obsidian 专属扩展，docx 不涉及 |
| 生成/编辑 .docx / .dotx Word 文件 | docx | 输出 Office 原生格式，可在 Word/WPS 打开 |
| 需要目录页码、修订、套 Word 模板 | docx | Word 排版能力，Markdown 不承担 |

**规则**：按**目标文件格式**分流——产物留在 Obsidian 知识库里的纯文本笔记用 obsidian-markdown；需要交付 .docx 给他人用 Word 打开的用 docx。标准 Markdown 语法（标题、加粗、列表、表格）属于默认能力，两个 skill 都不重复教学。

---

## 二、常用场景 Playbook

### 场景 A：从零做一个产品演示

```
brainstorming          → 发想内容和结构
  ↓
frontend-design        → 定视觉方向
  ↓
ui-ux-pro-max          → 选色板、字体、图标
  ↓
frontend-slides        → 输出 HTML 演示文稿
  ↓
handoff                → 生成交接文档（如需换设备继续）
```

### 场景 B：审查和改进现有 Web 页面

```
web-design-guidelines  → 全面 UI 审查
  ↓
accessibility          → 无障碍专项检查
  ↓
adversarial-ux-test    → 扮演恶意用户找痛点
  ↓
prototype              → 快速验证修复方案
```

### 场景 C：架构重构

```
improve-codebase-architecture → 扫描浅模块，生成 HTML 报告
  ↓
codebase-design               → 查设计原则指导修改
  ↓
grill-with-docs              → 拷问修改方案，产出 ADR
  ↓
tdd                           → 测试驱动实现修改
```

### 场景 D：A股投研全流程

```
market-daily-review       → 收盘复盘，发现市场热点
  ↓
a-share-stock-dossier     → 深挖热点个股基本面
  ↓
futures-deepview-analyst  → 期货对冲研判（如需）
```

### 场景 E：Bug 修复

```
diagnosing-bugs           → 系统化诊断问题根因
  ↓
prototype                 → 快速验证修复方案
  ↓
tdd                        → 测试驱动修复
```

### 场景 F：创建新 Skill

```
find-skills               → 先搜索是否已有类似 skill
  ↓
cangjie-skill             → 如原料是书/课程，先蒸馏
  ↓
skill-creator             → 创建/优化/评估新 skill
  ↓
improve-claude-md         → 优化项目的 CLAUDE.md 指令
```

### 场景 G：档案系统规划与建设

```
archives-lifecycle        → 总纲：梳理收管存用全流程
  ↓
archives-yidang-yiti     → 业档一体：业务系统对接与自动归档
  ↓
archives-pre-archiving    → 预归档：收集前置与三级协作
  ↓
archives-permissions      → 权限：分级分权与全宗管理
  ↓
archives-access-control   → 利用：借阅、水印、原文遮盖
  ↓
archives-four-tests       → 合规：四性检测与 DA/T70 把关
```

> 数字化转型项目额外使用 `archives-dual-to-single` 规划双套转单套路径。

---

## 三、简化触发词规则

为减少误触发，约定以下触发词：

| 说法 | 触发 Skill | 不触发 |
|---|---|---|
| "做演示" / "做 slides" | frontend-slides | ppt-generation |
| "做 PPT 文件" / "生成 PPTX" | ppt-generation | frontend-slides |
| "设计方向" / "美学指导" | frontend-design | ui-ux-pro-max |
| "选色板" / "选字体" / "选图标" | ui-ux-pro-max | frontend-design |
| "拷问我" / "stress-test" | grill-with-docs | grill-me, grilling |
| "给我看看" / "解释一下" | show-me | diagram-maker |
| "画流程图" / "画架构图" | diagram-maker | show-me |
| "审查 UI" / "检查设计" | web-design-guidelines | accessibility |
| "无障碍检查" / "WCAG" | accessibility | web-design-guidelines |
| "改进架构" / "扫描架构" | improve-codebase-architecture | codebase-design |
| "设计原则" / "模块设计" | codebase-design | improve-codebase-architecture |
| "收管存用" / "档案系统规划" | archives-lifecycle | 其他 archives-* |
| "业档一体" / "自动归档" | archives-yidang-yiti | archives-pre-archiving |
| "预归档" / "兼职档案员" | archives-pre-archiving | archives-yidang-yiti |
| "档案权限" / "分级分权" | archives-permissions | archives-access-control |
| "档案借阅" / "水印" / "原文遮盖" | archives-access-control | archives-permissions |
| "四性检测" / "档案合规" | archives-four-tests | 其他 archives-* |
| "双套制" / "单套制" / "档案数字化转型" | archives-dual-to-single | 其他 archives-* |
| "拆书" / "把书做成 skill" | cangjie-skill | skill-creator |
| "创建 skill" / "评测 skill" | skill-creator | cangjie-skill |
| "找技能" / "有没有做 X 的 skill" | find-skills | skill-creator |
| "写 Obsidian 笔记" / "双链" / "callout" / "frontmatter 属性" | obsidian-markdown | docx |
| "写 Word 文档" / "生成 .docx" / "Word 排版" | docx | obsidian-markdown |
| "算命" / "八字" / "紫微" / "排盘" | fortune | （独立，无冲突） |
| "A股复盘" / "收盘总结" | market-daily-review | a-share-stock-dossier |
| "个股尽调" / "个股体检" | a-share-stock-dossier | market-daily-review |
| "期货研判" / "主力合约" | futures-deepview-analyst | （独立） |
| "融资 BP" / "投资人备忘录" | investor-materials | （独立） |
| "风险评估" / "risk register" | risk-assessment | （独立） |

---

## 四、可考虑"休眠"的 Skill

以下 skill 功能已被其他 skill 覆盖，日常使用中不需要手动触发：

| Skill | 原因 | 状态 |
|---|---|---|
| grill-me | 功能被 grill-with-docs 完全覆盖 | 保留但不主动触发 |
| grilling | 作为 grill-with-docs 的内部依赖被自动调用 | 保留但不主动触发 |

其余 **40 个 skill** 都有独立不可替代的功能，全部保留。完整清单见 [SKILLS-INDEX.md](./SKILLS-INDEX.md)。

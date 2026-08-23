# Skill 使用策略

> 基于 33 个 skill 的 6 组冲突分析，制定明确的使用优先级和触发规则。

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
tdd                           → 测试驱动开发实现修改
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
skill-creator             → 创建/优化/评估新 skill
  ↓
improve-claude-md         → 优化项目的 CLAUDE.md 指令
```

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

---

## 四、可考虑"休眠"的 Skill

以下 skill 功能已被其他 skill 覆盖，日常使用中不需要手动触发：

| Skill | 原因 | 状态 |
|---|---|---|
| grill-me | 功能被 grill-with-docs 完全覆盖 | 保留但不主动触发 |
| grilling | 作为 grill-with-docs 的内部依赖被自动调用 | 保留但不主动触发 |

其余 31 个 skill 都有独立不可替代的功能，全部保留。

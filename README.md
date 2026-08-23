# My Agent Skills

个人 Agent Skill 仓库，用于跨设备同步和复用。

## 已收录 Skill

| Skill 名称 | 作者 | 来源 | 说明 |
| --- | --- | --- | --- |
| ui-ux-pro-max | nextlevelbuilder | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | UI/UX 设计智能技能，覆盖风格、配色、字体、UX 规则、动画预设、图表推荐等 |
| brainstorming | obra | https://github.com/obra/superpowers | 创意头脑风暴技能，在实现任何功能前先探索需求、设计方案、获取用户批准，支持 spike/bounded/architectural 三种路径 |
| frontend-slides | affaan-m | https://github.com/affaan-m/ECC | 创建动画丰富的 HTML 演示文稿，支持从零创建或 PPT/PPTX 转换，内置 12 种风格预设 |
| skill-creator | anthropics | https://github.com/anthropics/skills | 创建、修改和优化 Skill 的元技能，支持测试用例、评估基准、描述优化 |
| ppt-generation | bytedance | https://github.com/bytedance/deer-flow | AI 图片生成 + PPTX 组装，逐张生成幻灯片图片并合成 PowerPoint 文件 |
| vercel-react-best-practices | vercel-labs | https://github.com/vercel-labs/agent-skills | React/Next.js 性能优化规则集，70 条规则覆盖 8 个类别（异步瀑布、包体积、SSR、重渲染等） |
| docx | anthropics | https://github.com/anthropics/skills | Word 文档创建、编辑、分析，支持 tracked changes、批注、XSD 验证、pandoc 转换 |
| frontend-design | anthropics | https://github.com/anthropics/skills | 前端视觉设计指导，强调独特性、排版、配色、动效的刻意选择，避免模板化默认风格 |
| adversarial-ux-test | NousResearch | https://github.com/NousResearch/hermes-agent | 对抗式 UX 测试，扮演最挑剔用户发现体验痛点，经实用主义过滤后输出可执行工单 |
| risk-assessment | anthropics | https://github.com/anthropics/knowledge-work-plugins | 运营风险评估，识别、评估、规划缓解措施，含风险矩阵、6 大风险类别、风险登记册格式 |
| investor-materials | affaan-m | https://github.com/affaan-m/ECC | 投资人材料生成，创建 pitch deck、one-pager、投资人备忘录、财务模型、加速器申请，确保多份融资材料数据一致 |
| weather-reporter | awslabs | https://github.com/awslabs/agentcore-samples | 天气信息格式化，用 emoji 展示天气、双温标显示、基于天气的活动推荐和穿衣建议 |
| diagram-maker | openclaw | https://github.com/openclaw/openclaw | 图表绘制，支持 SVG/HTML 架构图和 Excalidraw 手绘白板，自动选择布局和语义配色 |
| accessibility | affaan-m | https://github.com/affaan-m/ECC | WCAG 2.2 Level AA 无障碍设计标准，跨平台（Web/iOS/Android）ARIA 映射、审计检查清单、反模式避坑 |
| fortune | ai-freer | https://github.com/ai-freer/fortune-skill | 中国传统命理分析（八字+紫微斗数），对话式收集出生信息，排盘脚本获取精确数据，结合九本经典典籍综合分析 |
| grill-me | mattpocock | https://github.com/mattpocock/skills | 计划/设计淬炼面试入口，重定向到 grilling 会话 |
| grilling | mattpocock | https://github.com/mattpocock/skills | relentless interview 核心引擎，设计树+frontier 逐轮拷问，自动分离事实查找与决策，直到达成共识 |

## 目录结构

```
.agents/skills/
├── ui-ux-pro-max/              # UI/UX 设计技能
│   ├── SKILL.md
│   ├── data/                   # 数据集（风格、色板、字体等）
│   ├── references/             # 参考文档
│   └── scripts/                # 搜索脚本
└── brainstorming/              # 头脑风暴技能
    ├── SKILL.md
    ├── visual-companion.md     # 可视化辅助指南
    ├── spec-document-reviewer-prompt.md  # Spec 评审模板
    └── scripts/                # 可视化伴侣服务器脚本
└── frontend-slides/            # HTML 演示文稿技能
    ├── SKILL.md
    ├── STYLE_PRESETS.md         # 12 种风格预设 + CSS 基础
    ├── animation-patterns.md   # 动画模式参考
    ├── html-template.md        # HTML 模板
    ├── viewport-base.css        # 视口适配 CSS
    ├── agents/openai.yaml      # OpenAI agent 配置
    └── scripts/                # PDF 导出 + PPTX 提取脚本
└── skill-creator/              # Skill 创建与优化技能
    ├── SKILL.md
    ├── LICENSE.txt              # Apache 2.0 许可证
    ├── agents/                  # 评估角色（分析器、比较器、评分器）
    ├── assets/                  # 评估查看器 HTML
    ├── eval-viewer/             # 评估结果查看器
    ├── references/              # Schema 文档
    └── scripts/                 # 评估、基准、描述优化脚本
└── ppt-generation/              # PPT 生成技能（AI 图片 + PPTX 组装）
    ├── SKILL.md
    └── scripts/generate.py      # PPTX 组装脚本
└── vercel-react-best-practices/  # React/Next.js 性能优化技能
    ├── SKILL.md
    ├── AGENTS.md                 # 编译后的完整规则文档
    ├── metadata.json             # 版本元数据
    └── rules/                    # 70 条规则文件（8 个类别）
└── docx/                          # Word 文档技能
    ├── SKILL.md
    ├── LICENSE.txt                # 专有许可证
    └── scripts/                  # 工具链
        ├── accept_changes.py      # 接受修订
        ├── comment.py             # 批注
        ├── merge_runs.py          # 合并文本片段
        └── office/                # Office 共享模块
            ├── soffice.py         # LibreOffice 封装
            ├── validate.py        # XSD 验证器
            ├── validators/        # docx/pptx/redlining 验证器
            └── schemas/           # ISO IEC29500 XML Schema
└── frontend-design/              # 前端视觉设计技能
    ├── SKILL.md
    └── LICENSE.txt
└── adversarial-ux-test/          # 对抗式 UX 测试技能
    └── SKILL.md
└── risk-assessment/              # 运营风险评估技能
    └── SKILL.md
└── investor-materials/           # 投资人材料技能
    ├── SKILL.md
    └── agents/openai.yaml
└── weather-reporter/             # 天气报告技能
    └── SKILL.md
└── diagram-maker/               # 图表绘制技能
    ├── SKILL.md
    └── references/               # SVG 模板 + Excalidraw 模式参考
└── fortune/                      # 中国传统命理分析技能（八字+紫微斗数）
    ├── SKILL.md                   # 完整交互流程与分析框架（41KB）
    ├── AGENTS.md                  # Codex agent 指引
    ├── CLAUDE.md                  # Claude Code agent 指引
    ├── INSTALL.md                 # 分平台安装指引
    ├── install.sh                 # 一键安装脚本
    ├── package.json               # Node.js 依赖（iztro, lunar-javascript）
    ├── requirements.txt           # Python 依赖（lunar-python 等）
    ├── scripts/                   # 19 个排盘/报告/验证脚本
    │   ├── bazi-chart.mjs         # 八字排盘（lunar-javascript）
    │   ├── ziwei-chart.mjs        # 紫微斗数排盘（iztro）
    │   ├── bazi-classic.py        # 三命通会论断（china-testing/bazi）
    │   ├── time-normalize.mjs     # 真太阳时校正
    │   ├── fortune-report-data.mjs # 报告数据聚合
    │   ├── hecan-summary.mjs      # 结构化合参 v2 判断卡片
    │   ├── hecan-audit.mjs       # 合参审计
    │   ├── rule-matcher.mjs      # 经典规则命中匹配
    │   ├── report-draft.mjs       # 报告草稿生成
    │   ├── report-qa.mjs         # 报告质量检查
    │   ├── privacy-check.mjs     # 隐私检查
    │   └── ...                    # 其他辅助脚本
    ├── references/                # 命理知识库（11 个文件）
    │   ├── classical-texts.md     # 九本经典典籍核心规则摘要
    │   ├── classical-rules.json   # 调候/格局/病药结构化规则
    │   ├── bazi-guide.md          # 八字命理分析指南
    │   ├── ziwei-guide.md        # 紫微斗数解盘指南
    │   ├── wuxing-tables.md      # 五行/天干地支/十神参考表
    │   ├── methodology-framework.json # 方法论核对框架
    │   ├── report-templates.json  # 报告模板骨架
    │   └── ...                    # 其他参考文件
    └── vendor/bazi/              # china-testing/bazi 源码
        ├── bazi.py, sizi.py, ...  # 排盘+分析 Python 代码
        ├── books/                 # 子平真诠、穷通宝鉴等典籍
        └── examples/             # 格局示例
└── grill-me/                     # 计划/设计淬炼面试技能
    ├── SKILL.md                   # 重定向到 /grilling 会话
    └── agents/openai.yaml         # Codex 平台元数据
└── grilling/                     # relentless interview 核心引擎
    ├── SKILL.md                   # 设计树+frontier 逐轮拷问方法论
    └── agents/openai.yaml         # Codex 平台元数据
```

## 如何在新设备上使用

1. `git clone` 本仓库到本地
2. 将 `.agents/skills/` 目录放入你的项目中（或软链接到项目目录）
3. 在 TraeCode / TraeWork 中：设置 > 技能与命令 > 打开「启用 .agents 技能目录」开关

## 如何更新 Skill

```bash
# 更新单个 Skill 到最新版
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max --agent trae -y --copy

# 提交更新到本仓库
git add -A
git commit -m "update: ui-ux-pro-max"
git push
```

## 如何新增 Skill

将新 Skill 安装到 `.agents/skills/` 目录后，更新本 README 的收录列表，然后提交即可。

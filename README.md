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

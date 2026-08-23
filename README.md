# My Agent Skills

个人 Agent Skill 仓库，用于跨设备同步和复用。

## 已收录 Skill

| Skill 名称 | 作者 | 来源 | 说明 |
| --- | --- | --- | --- |
| ui-ux-pro-max | nextlevelbuilder | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | UI/UX 设计智能技能，覆盖风格、配色、字体、UX 规则、动画预设、图表推荐等 |
| brainstorming | obra | https://github.com/obra/superpowers | 创意头脑风暴技能，在实现任何功能前先探索需求、设计方案、获取用户批准，支持 spike/bounded/architectural 三种路径 |

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

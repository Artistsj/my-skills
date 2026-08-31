# 术语提取器候选 (Glossary candidates)

- id: g01
  term: 业档一体
  type: term
  source_chapter: 第2部分·"业档一体"解决方案
  author_definition: |
    "将档案管理与前端业务充分融合，实现各类业务场景的业档一体化，
    助力企业在全程数字化的背景之下，实现各个环节的无缝融合。
    前端业务系统当中的电子文件按照收集保管范围表，应收尽收、应归尽归。"
  key_distinction: |
    ≠ "业务系统和档案系统各管各的" — 不是简单的系统对接
    ≠ "把业务数据导入档案系统" — 不是单向的数据搬运
    = 业务流程与档案流程深度融合，业务办结即自动归档，档案数据反哺业务
  why_it_matters: |
    "业档一体"是本方案的核心概念，下游所有skill都会引用这个词。
    如果理解成简单的"系统集成"，会低估其架构深度和实施复杂度。
  tags: [term, core-concept]

- id: g02
  term: 预归档
  type: term
  source_chapter: 第20页·预归档管理
  author_definition: |
    "对于归档周期较长、自动分类规则不明确的档案，可预先进入预归档库，
    由兼职档案管理员或部门业务人员进行日常维护，保证档案完整性。
    设置预归档库中与接收库中的元数据字段映射关系，可进行批量组件、合并组件操作，
    并进行自动分类。"
  key_distinction: |
    ≠ "草稿" — 预归档是有管理标准的正式环节，不是随便存
    ≠ "临时文件夹" — 预归档有元数据、有分类规则、有审核流程
    = 业务系统和正式档案库之间的缓冲层，实现收集整理前置化
  why_it_matters: |
    预归档是实现"从单兵作战到系统作战"的关键机制。
    如果理解成"临时存放"，会忽略其在管理体系中的核心地位。
  tags: [term, pre-archiving, collection]

- id: g03
  term: 四性检测
  type: term
  source_chapter: 第28页·四性检测
  author_definition: |
    "按照DA/T70标准设计四性检测方案。主要检测归档文件的真实、完整、安全、可用。
    同时会出具相关的四性检测报告，以保证我们电子文件的合规性。"
  key_distinction: |
    ≠ "质量检查" — 不是泛泛的质量检查，而是有国家标准的合规检测
    ≠ "只做一次" — 贯穿移交接收、归档、长期保存三个环节
    = 基于DA/T70标准，对电子档案的真实性、完整性、安全性、可用性进行的标准化检测
  why_it_matters: |
    四性检测是电子档案合规性的核心保障，也是国家试点项目验收的必要条件。
    下游"四性检测框架"skill需要这个术语的准确定义。
  tags: [term, compliance, quality-control]

- id: g04
  term: 双套制 / 单套制
  type: term
  source_chapter: 第6页·助力双套制向单套制管理逐步过渡
  author_definition: |
    "电子档案单套管理：仅以电子形式归档和管理电子档案的方式。
    双套制=纸质档案+电子档案两套并行管理。"
  key_distinction: |
    ≠ "电子备份" — 单套制不是"有电子备份就行"，而是电子档案本身具有法律效力
    ≠ "不要纸质了" — 单套制是逐步过渡，不是一刀切全部电子化
    = 从纸质+电子双套并行，逐步过渡到纯电子单套管理的演进路径
  why_it_matters: |
    双套制向单套制过渡是档案数字化转型的核心命题。
    下游"双套制向单套制过渡框架"skill需要这个术语。
  tags: [term, digital-transformation, management-model]

- id: g05
  term: 全宗
  type: term
  source_chapter: 第43页·后台配置/档案设置
  author_definition: |
    "支持多全宗的管理，实现了档案的分级分权的管控。
    以及对于不同全宗之下，档案门类的灵活扩充和调整。"
  key_distinction: |
    ≠ "文件夹" — 不是简单的分类目录
    ≠ "部门" — 不是按组织部门划分
    = 一个机构（组织）形成的全部档案构成一个全宗，是档案管理的基本单位
  why_it_matters: |
    全宗是档案管理的基本组织单位，分级分权管理框架就是基于全宗构建的。
    不理解全宗概念，就无法正确理解档案权限体系。
  tags: [term, archives-management, basic-unit]

- id: g06
  term: 收管存用
  type: term
  source_chapter: 第3部分·产品功能简介
  author_definition: |
    "围绕档案的全生命周期管理，以档案的收、管、存、用为主，展开介绍。"
  key_distinction: |
    ≠ "四个功能模块" — 不是简单的功能划分，而是生命周期的四个阶段
    ≠ "互相独立" — 四个阶段是连续的、有流转关系的
    = 档案全生命周期管理的四个核心阶段：收集、管理、保存、利用
  why_it_matters: |
    "收管存用"是档案管理领域的标准框架，也是本方案的产品功能组织结构。
    所有下游skill都可以映射到这四个阶段中。
  tags: [term, lifecycle, framework]

- id: g07
  term: EEP数据包
  type: term
  source_chapter: 第33页·档案移交
  author_definition: |
    "支持跨系统离线移交，将需要导出的档案按照《电子档案移交与接收管理办法》
    导出数据包生成EEP数据包进行数据移交操作。"
  key_distinction: |
    ≠ "压缩包" — 不是简单的文件压缩，有标准的封装格式和元数据规范
    ≠ "备份文件" — 目的是移交接收，不是数据备份
    = 符合《电子档案移交与接收管理办法》的标准电子档案移交封装格式
  why_it_matters: |
    EEP数据包是档案跨系统移交和进馆的标准格式，也是合规验收的必要条件。
    理解这个术语才能正确理解档案移交和长期保存的机制。
  tags: [term, compliance, transfer-format]

- id: g08
  term: 原文遮盖
  type: term
  source_chapter: 第39页·利用控制
  author_definition: |
    "通过借阅流程进行档案的在线审批，系统支持在审批流程中对原文进行
    遮盖处理后生成【借阅副本】，遮盖时支持对内容涂抹、加入文本、上传图片等操作。"
  key_distinction: |
    ≠ "文件加密" — 不是加密文件，而是生成一个遮盖后的副本
    ≠ "权限控制" — 比简单的"能看/不能看"更细粒度，可以控制看到多少内容
    = 档案借阅中的细粒度内容控制手段，通过涂抹遮盖生成借阅副本
  why_it_matters: |
    原文遮盖是档案利用控制框架中的核心手段之一。
    理解这个术语才能完整理解档案权限控制的层次。
  tags: [term, access-control, utilization]

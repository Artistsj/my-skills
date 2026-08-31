# 原则提取器候选 (Principle candidates)

- id: p01
  title: 应收尽收、应归尽归
  type: principle
  source_chapter: 第46页·核心亮点·100%归档
  source_quote: |
    "将前端业务系统当中的电子文件按照收集保管范围表，应收尽收、应归尽归。"
  summary: |
    档案收集的第一原则：凡是符合收集保管范围表的电子文件，必须全部收集、全部归档，
    不遗漏任何有保存价值的业务数据。这是实现100%自动归档的前提。
    落地手段：通过集成引擎对接业务系统，预定义归档范围和规则。
  tags: [principle, collection, completeness]

- id: p02
  title: 收管存用全生命周期管理
  type: principle
  source_chapter: 第7页·数字档案的全生命周期管理
  source_quote: |
    "档案管理能够和流程结合起来，经过相关领导的审批、授权后由系统自动执行。"
  summary: |
    档案管理必须覆盖完整的生命周期，不能只管某一个环节。
    从收集→管理→保存→利用，每个环节都要有标准流程、有审批授权、有系统留痕，
    由系统自动执行而非人工操作，确保合规性和可追溯性。
  tags: [principle, lifecycle, process]

- id: p03
  title: 收集整理前置化
  type: principle
  source_chapter: 第20页·预归档管理
  source_quote: |
    "对于归档周期较长、自动分类规则不明确的档案，可预先进入预归档库，
    由兼职档案管理员或部门业务人员进行日常维护，保证档案完整性。"
  summary: |
    档案的收集和整理工作要尽可能前置到业务端，而不是等到最后由档案员统一处理。
    前端业务人员最了解业务背景，由他们在产生数据时就进行预整理，
    既能保证档案完整性，又能减少后端档案员的重复劳动。
  tags: [principle, front-loading, pre-archiving]

- id: p04
  title: 从单兵作战到系统作战
  type: principle
  source_chapter: 第49页·核心亮点·预归档平台
  source_quote: |
    "按照业务场景进行文件划分，从单兵作战向系统作战演进。"
  summary: |
    档案管理不能只靠档案员一个人或一个部门，要建立"业务人员→兼职档案员→专职档案员"
    的三级协作体系，让每个人在自己的环节做最适合的事。
    业务人员产生文件、兼职档案员预整理、专职档案员审核归档，形成系统作战。
  tags: [principle, organization, collaboration]

- id: p05
  title: 四性检测贯穿全流程
  type: principle
  source_chapter: 第28页·四性检测
  source_quote: |
    "按照DA/T70标准设计四性检测方案。主要检测归档文件的真实、完整、安全、可用。"
  summary: |
    电子档案的质量检测（真实性、完整性、安全性、可用性）不能只做一次，
    而要贯穿档案全生命周期的三个关键节点：
    档案移交与接收环节、档案归档环节、档案长期保存环节。
    每个环节都要做检测，不合格就退回，确保电子档案始终符合标准。
  tags: [principle, quality-control, compliance]

- id: p06
  title: 分级分权、按岗授权
  type: principle
  source_chapter: 第51页·核心亮点·分级分权
  source_quote: |
    "支持集团型组织按照档案不同全宗、门类对权限进行组合，
    可以单独控制每一个菜单和数据权限，授予不同组织、角色的用户对象。"
  summary: |
    档案权限管理要做到多维度、精细化，不能一概而论。
    不同全宗、不同门类、不同岗位、不同角色，权限都应该不一样。
    权限颗粒度要细到菜单级、数据级，按需授权，而不是要么全有权要么全没有。
  tags: [principle, permissions, authorization]

- id: p07
  title: 业档融合、双向赋能
  type: principle
  source_chapter: 第14页·全程数字化业档一体档案管理平台
  source_quote: |
    "在线接收、反哺业务、业务处理、系统反馈。"
  summary: |
    档案系统和业务系统不是单向的"业务→档案"归档关系，而是双向融合：
    正向——业务办结后自动归档到档案系统
    反向——档案系统的数据可以被业务系统安全调用，支撑业务决策
    只有双向打通，档案才能从"死数据"变成"活资产"。
  tags: [principle, integration, data-value]

- id: p08
  title: 数字防篡改、可信身份
  type: principle
  source_chapter: 第47页·核心亮点·数字防篡改
  source_quote: |
    "基于自主的电子签名核心技术，为收集到的电子文件加盖电子签名，
    赋予每一份电子档案防篡改的能力。"
  summary: |
    电子档案要具备法律效力，必须解决防篡改问题。
    通过数字签名和电子印章技术，为每一份电子档案加盖可信身份认证，
    确保档案内容不被篡改、来源可追溯、身份可验证。
    这是电子档案从"辅助参考"走向"法律凭证"的核心前提。
  tags: [principle, security, anti-tamper, legal-effect]

# 围棋教材个人知识库

## 概况

- 书籍: 围棋（第一册）— 邱百瑞 著
- 总页数: 234 页（扫描版 PDF，无文字层）
- OCR 引擎: PaddleOCR PP-OCRv6（oneDNN 禁用）
- 识别准确率: 92%-100%（平均 96%+）
- 处理状态: 已处理 10/234 页（演示）

## 目录结构

```
knowledge-base/
├── metadata.json          # 书籍元数据
├── index.json             # 全文搜索索引
├── images/                # 每页 300 DPI 图片
│   ├── page_0001.png
│   ├── page_0002.png
│   └── ...
└── text/                  # OCR 识别文字
    ├── page_0001.txt      # 纯文本
    ├── page_0001.json     # 含置信度的 JSON
    └── ...
```

## 搜索测试结果

| 关键词 | 命中页数 | 示例 |
|---|---|---|
| 围棋 | 5 | 第1页: "中国围棋协会培训中心指定教材" |
| 气 | 5 | 第9页: "棋子在棋盘上，与它有直线相连并紧邻此子的空交叉点" |
| 提子 | 3 | 第11页: "气尽提子。任何一部分棋子只要成为无气状态，就应立即提掉" |
| 连接 | 1 | 第9页: "连接与切断" |
| 眼 | 1 | 第13页: "眼、活棋。由一方的子围成若干的点" |
| 活棋 | 1 | 第13页: "敌方一旦入侵就能立即加以歼灭" |
| 断 | 3 | 第11页: "白1把黑方两个有可能相连的子分割开，术语称为'断'" |

## 完整处理方法

### 环境要求

```bash
pip install pymupdf paddlepaddle paddleocr --break-system-packages
# PaddleOCR 需要 oneDNN 禁用才能正常运行
```

### 处理全部 234 页

```bash
# 在脚本所在目录运行
FLAGS_use_mkldnn=0 \
FLAGS_enable_pir_api=0 \
FLAGS_enable_pir_in_executor=0 \
python3 knowledge_base_builder.py --start 1 --end 234
```

每页约 40-60 秒，234 页约需 3-4 小时。建议分批处理：

```bash
# 第一批
python3 knowledge_base_builder.py --start 1 --end 50
# 第二批
python3 knowledge_base_builder.py --start 51 --end 100
# ...以此类推
```

脚本支持增量处理：已处理的页会被跳过，索引会自动合并。

### 搜索知识库

```python
import json

with open("knowledge-base/index.json") as f:
    index = json.load(f)

query = "提子"
for page in index["pages"]:
    if query in page["text"]:
        pos = page["text"].find(query)
        context = page["text"][max(0,pos-40):pos+40]
        print(f"第 {page['page']} 页: {context}")
```

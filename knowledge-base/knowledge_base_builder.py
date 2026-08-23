#!/usr/bin/env python3
"""
Personal Knowledge Base Builder — 围棋教材 PDF → 可检索知识库
Processes scanned PDF: extract images + OCR text + build search index.

Usage:
  python3 knowledge_base_builder.py                    # Process all pages
  python3 knowledge_base_builder.py --start 1 --end 20 # Process pages 1-20
"""

import os
os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["FLAGS_enable_pir_in_executor"] = "0"

import warnings
warnings.filterwarnings("ignore")

import fitz
import json
import argparse
import time
from pathlib import Path

# === Config ===
PDF_PATH = "/workspace/.uploads/130e8433-5691-45cd-bc62-df74adb3073a_围棋(第一册)(邱百瑞).pdf"
KB_ROOT = Path("/workspace/knowledge-base")
IMAGES_DIR = KB_ROOT / "images"
TEXT_DIR = KB_ROOT / "text"
INDEX_PATH = KB_ROOT / "index.json"
META_PATH = KB_ROOT / "metadata.json"

# Create dirs
for d in [IMAGES_DIR, TEXT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def extract_page_image(doc, page_num, dpi=300):
    """Extract page as PNG image at given DPI."""
    page = doc[page_num]
    mat = fitz.Matrix(dpi/72, dpi/72)
    pix = page.get_pixmap(matrix=mat)
    img_path = IMAGES_DIR / f"page_{page_num+1:04d}.png"
    pix.save(str(img_path))
    return img_path, pix.width, pix.height

def ocr_page(img_path, ocr_engine):
    """Run PaddleOCR on a page image, return text lines with confidence."""
    results = list(ocr_engine.predict(str(img_path)))
    
    all_lines = []
    for result in results:
        res = result.json.get('res', result.json)
        texts = res.get('rec_texts', [])
        scores = res.get('rec_scores', [1.0]*len(texts))
        
        for text, score in zip(texts, scores):
            all_lines.append({
                "text": text,
                "confidence": round(score, 2)
            })
    
    return all_lines

def save_page_text(page_num, lines):
    """Save OCR text for a page as both raw and formatted."""
    # Raw text (all lines joined)
    raw_path = TEXT_DIR / f"page_{page_num+1:04d}.txt"
    with open(raw_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line['text']}\n")
    
    # JSON with confidence scores
    json_path = TEXT_DIR / f"page_{page_num+1:04d}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lines, f, ensure_ascii=False, indent=2)

def build_index(page_data_list):
    """Build a search index from all processed pages."""
    # Full-text index: list of {page, text, keywords}
    index = {
        "book_title": "围棋（第一册）",
        "author": "邱百瑞",
        "total_pages": page_data_list[0]["total_pages"] if page_data_list else 0,
        "processed_pages": len(page_data_list),
        "pages": []
    }
    
    # Collect all keywords by page
    for pd in page_data_list:
        page_text = " ".join([l["text"] for l in pd["lines"]])
        index["pages"].append({
            "page": pd["page_num"],
            "text": page_text,
            "char_count": len(page_text),
            "avg_confidence": round(
                sum(l["confidence"] for l in pd["lines"]) / max(len(pd["lines"]), 1), 2
            ),
            "image": f"images/page_{pd['page_num']:04d}.png",
            "text_file": f"text/page_{pd['page_num']:04d}.txt"
        })
    
    return index

def search_index(query, index):
    """Simple keyword search across all pages."""
    results = []
    query_lower = query.lower()
    
    for page in index["pages"]:
        text_lower = page["text"].lower()
        if query_lower in text_lower:
            # Find surrounding context
            pos = text_lower.find(query_lower)
            start = max(0, pos - 50)
            end = min(len(page["text"]), pos + len(query_lower) + 50)
            context = page["text"][start:end]
            
            results.append({
                "page": page["page"],
                "context": context,
                "image": page["image"],
                "confidence": page["avg_confidence"]
            })
    
    return sorted(results, key=lambda x: x["page"])

def main():
    parser = argparse.ArgumentParser(description="Build knowledge base from scanned PDF")
    parser.add_argument("--start", type=int, default=1, help="Start page (1-indexed)")
    parser.add_argument("--end", type=int, default=None, help="End page (1-indexed)")
    args = parser.parse_args()
    
    doc = fitz.open(PDF_PATH)
    total_pages = doc.page_count
    end_page = args.end or total_pages
    
    print(f"=== 围棋知识库构建 ===")
    print(f"PDF: {PDF_PATH}")
    print(f"总页数: {total_pages}")
    print(f"处理范围: 第 {args.start} 页 - 第 {end_page} 页")
    print(f"输出目录: {KB_ROOT}")
    print()
    
    # Initialize PaddleOCR
    print("初始化 PaddleOCR...")
    from paddleocr import PaddleOCR
    ocr = PaddleOCR(lang='ch', enable_mkldnn=False)
    print("PaddleOCR 就绪\n")
    
    # Process pages
    all_page_data = []
    
    for page_num in range(args.start - 1, end_page):
        t0 = time.time()
        print(f"处理第 {page_num + 1}/{end_page} 页...", end=" ", flush=True)
        
        # 1. Extract image
        img_path, w, h = extract_page_image(doc, page_num)
        
        # 2. OCR
        lines = ocr_page(img_path, ocr)
        
        # 3. Save text
        save_page_text(page_num, lines)
        
        # 4. Collect data for index
        all_page_data.append({
            "page_num": page_num + 1,
            "lines": lines,
            "total_pages": total_pages
        })
        
        avg_conf = sum(l["confidence"] for l in lines) / max(len(lines), 1)
        elapsed = time.time() - t0
        print(f"{len(lines)} 行, 平均置信度 {avg_conf:.2f}, {elapsed:.1f}s")
    
    doc.close()
    
    # Build index
    print(f"\n构建搜索索引...")
    index = build_index(all_page_data)
    
    # Load existing index if any (for incremental processing)
    existing_pages = {}
    if INDEX_PATH.exists():
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            old_index = json.load(f)
        for p in old_index.get("pages", []):
            existing_pages[p["page"]] = p
    
    # Merge: new pages overwrite old
    for p in index["pages"]:
        existing_pages[p["page"]] = p
    
    # Sort by page number
    index["pages"] = sorted(existing_pages.values(), key=lambda x: x["page"])
    index["processed_pages"] = len(index["pages"])
    
    # Save index
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    # Save metadata
    meta = {
        "book_title": "围棋（第一册）",
        "author": "邱百瑞",
        "publisher": "中国统计出版社",
        "isbn": "7-5037-3010-2/G.74",
        "total_pages": total_pages,
        "processed_pages": len(index["pages"]),
        "ocr_engine": "PaddleOCR PP-OCRv6",
        "dpi": 300,
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 完成 ===")
    print(f"已处理: {len(all_page_data)} 页 (累计 {len(index['pages'])} 页)")
    print(f"图片: {IMAGES_DIR}/")
    print(f"文本: {TEXT_DIR}/")
    print(f"索引: {INDEX_PATH}")
    print(f"元数据: {META_PATH}")
    
    # Demo search
    if all_page_data:
        print(f"\n=== 搜索测试: '气' ===")
        results = search_index("气", index)
        print(f"找到 {len(results)} 页包含 '气'")
        for r in results[:5]:
            print(f"  第 {r['page']} 页: ...{r['context']}...")
    
    print(f"\n=== 全部完成 ===")

if __name__ == "__main__":
    main()

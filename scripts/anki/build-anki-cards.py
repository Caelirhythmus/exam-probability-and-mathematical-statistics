"""
Anki 制卡工具
将 collections.md 转换为 Anki 可导入的 TSV 文件。
每条记录生成 2 张卡：「主题 → 路径」「求解 → 路径」。
"""

import os
import re

def find_collections_file(start_dir="."):
    """从工作目录开始，查找 collections.md"""
    for root, dirs, files in os.walk(start_dir):
        if "collections.md" in files:
            return os.path.join(root, "collections.md")
    return None

def parse_records(text):
    """将文本解析为记录列表，每条记录含主题、求解、路径"""
    records = []
    blocks = re.split(r"\n\s*\n", text.strip())
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        topic = solve = path = None
        for line in lines:
            line = line.strip()
            if line.startswith("主题："):
                topic = line[len("主题："):].strip()
            elif line.startswith("求解："):
                solve = line[len("求解："):].strip()
            elif line.startswith("路径："):
                path = line[len("路径："):].strip()
        if topic and solve and path:
            records.append((topic, solve, path))
    return records

def main():
    src = find_collections_file()
    if not src:
        print("未在当前工作目录下找到 collections.md")
        return

    print(f"找到文件：{src}")

    with open(src, encoding="utf-8") as f:
        text = f.read()

    records = parse_records(text)
    if not records:
        print("未解析到任何有效记录（每卡需包含主题、求解、路径三行）")
        return

    output_path = os.path.join(os.path.dirname(src) or ".", "anki-cards.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("正面\t背面\n")
        for topic, solve, path in records:
            f.write(f"主题：{topic}\t路径：{path}\n")
            f.write(f"求解：{solve}\t路径：{path}\n")

    print(f"已生成 {len(records) * 2} 张卡片 → {output_path}")

if __name__ == "__main__":
    main()

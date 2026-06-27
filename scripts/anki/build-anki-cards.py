"""
Anki 制卡工具
将 cards/ 目录下所有 .md 卡文件合并为 Anki 可导入的 TSV。
每条记录生成 1 张卡，正面同时显示「主题」和「求解」。
"""

import os
import re
import glob

def find_cards_dir(start_dir="."):
    """从工作目录开始，查找 cards/ 目录"""
    for root, dirs, files in os.walk(start_dir):
        if os.path.basename(root) == "1-cards":
            return root
    # 回退：直接检查 1-collections/cards/
    candidate = os.path.join(start_dir, "1-collections", "1-cards")
    if os.path.isdir(candidate):
        return candidate
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
    cards_dir = find_cards_dir()
    if not cards_dir:
        print("未找到 cards/ 目录")
        return

    card_files = sorted(glob.glob(os.path.join(cards_dir, "*.md")))
    if not card_files:
        print("cards/ 目录下没有 .md 文件")
        return

    print(f"找到 cards 目录：{cards_dir}")
    all_records = []
    for fpath in card_files:
        fname = os.path.basename(fpath)
        with open(fpath, encoding="utf-8") as f:
            records = parse_records(f.read())
        print(f"  {fname} → {len(records)} 张卡片")
        all_records.extend(records)

    if not all_records:
        print("未解析到任何有效记录")
        return

    output_path = os.path.join(cards_dir, "..", "anki-cards.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for topic, solve, path in all_records:
            front = f"主题：{topic}  求解：{solve}"
            back = f"路径：{path}"
            f.write(f"{front}\t{back}\n")

    print(f"\n已生成 {len(all_records)} 张卡片 → {output_path}")

if __name__ == "__main__":
    main()

import os
import re
import shutil

# =============== CONFIG ===============

SOURCE_DIR = "problems"
CATEGORY_MAP = {
    "array": ["two sum", "3sum", "product", "rotate", "subarray", "contains duplicate"],
    "hash": ["anagram", "isomorphic", "hash", "map", "set"],
    "sliding_window": ["substring", "anagram", "window"],
    "dp": ["climb", "rob", "palindrome", "dp", "longest", "subsequence"],
    "tree": ["tree", "bst", "binary", "depth", "invert"],
    "graph": ["graph", "island", "clone"],
}

DEFAULT_CATEGORY = "misc"

# =====================================


def normalize_filename(filename: str):
    """
    Convert VS Code default name to:
    0001_two_sum.py
    """
    # extract number and name
    match = re.match(r"(\d+)[-_](.+)\.py", filename)
    if not match:
        return None

    num, title = match.groups()

    num = num.zfill(4)
    title = title.lower().replace("-", "_").replace(" ", "_")

    return f"{num}_{title}.py"


def detect_category(title: str):
    """
    Find category according to keywords.
    """
    title_lower = title.lower()

    for cat, keywords in CATEGORY_MAP.items():
        for k in keywords:
            if k in title_lower:
                return cat

    return DEFAULT_CATEGORY


def main():
    print("=== Sorting LeetCode files ===")

    for file in os.listdir(SOURCE_DIR):
        src_path = os.path.join(SOURCE_DIR, file)

        # only process python files in root problems directory
        if not os.path.isfile(src_path) or not file.endswith(".py"):
            continue

        # skip already categorized files
        if "_" in file and file.split("_")[0].isdigit() and len(file.split("_")[0]) == 4:
            print(f"[SKIP] Already sorted: {file}")
            continue

        # normalize file name
        new_name = normalize_filename(file)
        if not new_name:
            print(f"[SKIP] Unrecognized file: {file}")
            continue

        # determine category
        title_part = new_name[5:-3]  # remove "0001_" and ".py"
        category = detect_category(title_part)

        # ensure category directory exists
        category_dir = os.path.join(SOURCE_DIR, category)
        os.makedirs(category_dir, exist_ok=True)

        # move file
        dst_path = os.path.join(category_dir, new_name)
        print(f"[MOVE] {file} → {dst_path}")

        shutil.move(src_path, dst_path)

    print("=== Done! ===")


if __name__ == "__main__":
    main()

import os

base = "problems"
lines = []

for cat in sorted(os.listdir(base)):
    cat_dir = os.path.join(base, cat)
    if not os.path.isdir(cat_dir):
        continue

    lines.append(f"## {cat.title()}")
    for file in sorted(os.listdir(cat_dir)):
        pid, slug = file.split('_', 1)
        title = slug.replace(".py", "").replace('_', ' ').title()
        lines.append(f"- [{pid} {title}](problems/{cat}/{file})")
    lines.append("")

introduce = "本仓库用于系统性管理 LeetCode 刷题过程，采用工程化题解模板与分类目录结构，便于长期维护与记录总结。"
readme = "# LeetCode Python Solutions\n\n" + introduce + "\n\n" + "\n".join(lines)

with open("README.md", "w") as f:
    f.write(readme)

print("README updated!")

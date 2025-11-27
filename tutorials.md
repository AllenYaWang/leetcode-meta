# tutorials

## how to use

tool

## work flow

你的完整刷题执行流程如下：

```css
打开 VS Code → 选题 → Code Now → 写题 → 运行 Demo → 自动归类脚本 → 更新 README → Git 提交 → 推送 GitHub
```

每次做题只需要 2 分钟额外操作，就能让你的仓库保持专业、清晰、工程化。

下面一步步展开。

### 🧠 Step 1：VS Code 中挑选题目（最快切入）

使用 LeetCode 插件的优势：

- 题目分类清晰

- 支持每日一题

- 支持过滤（例如 “Medium only”）

- 支持快速搜索

- 点击就打开远程题目描述

点击 “Code Now” 后自动创建文件：

```shell
leetcode-meta/problems/123_title.py
```

你无需创建目录，插件自动搞定。

### 🧩 Step 2：填入 Python 模板（使用 snippet：lc）

你使用我为你准备的 snippet：

输入：
```shell
lc
```

自动展开成：
```python
# -*- coding: utf-8 -*-
"""
LeetCode: {}
Difficulty: {}
URL: {}

Approach:
1.
2.
3.

Time Complexity: O()
Space Complexity: O()
"""

from typing import *

class Solution:
    def XXX(self, ...):
        pass
```

👇 好处：

- 所有题目风格一致

- 思路写在顶层，面试必考

- typing 能体现工程素养

- 代码更易读

- GitHub 显示更专业

### 🧪 Step 3：写题 & 运行本地 Demo（1–2 分钟）

在文件末尾写你的小测试：

if __name__ == "__main__":
    sol = Solution()
    print(sol.function(...))


在 VS Code 内置终端运行：

```shell
python 123_title.py
```

快速验证正确性。

### ⚙️ Step 4：运行自动归类脚本

你运行：

```shell
python tools/sort_leetcode.py
```

🌟 脚本自动：

- 重命名 → 0123_valid_parentheses.py

- 归类 → problems/stack/0123_valid_parentheses.py

- 整理目录结构

- 保持仓库整洁

- 你完全不需要手动整理题目。

### 📚 Step 5：自动生成 README 索引（可选）

```python
python tools/generate_readme_index.py
```

生成一份炫酷、自动化维护的索引：

```css
## Array
- [0001 Two Sum](problems/array/0001_two_sum.py)
- [0015 3Sum](problems/array/0015_3sum.py)

## Hash
- [0242 Valid Anagram](problems/hash/0242_valid_anagram.py)
```

GitHub 看起来非常专业。

### 📌 Step 6：Git 提交（保持高质量 commit message）

推荐：
```shell
git add .
git commit -m "feat: add 0123 valid parentheses (stack medium)"
git push
```

规范、专业、可展示。

⭐ Step 7：每日回顾（10 分钟）

每晚用以下流程 review：

1. 看昨天的 3–5 个题解

2. 再默写 1 个关键题（如滑动窗口、二叉树）

3. 更新 “重点题目” 列表

这样做可以让你两周后接近“机械性熟练度”。

### 🎯 全套工作流流程图
```css
[选题] 
   ↓
[VS Code Code Now 自动生成文件]
   ↓
[lc snippet 自动生成模板]
   ↓
[写题 + 测试]
   ↓
[自动归类 sort_leetcode.py]
   ↓
[更新 README]
   ↓
[git commit + push]
   ↓
[每日回顾]
```

🔥 这个流程为什么最高效？
1. 完全不打断刷题节奏
   - 无需创建文件夹
   - 无需考虑命名
   - 无需整理目录

你只管做题。

🧠 2. 工程化体系

你的仓库最终呈现出：

problems/
  array/
  dp/
  tree/
  graph/
  sliding_window/


这展示了：

你的系统化能力

你的工程实践能力

你的学习能力

你的规范性

这些是大厂面试官非常看重的。

🧩 3. 对你两周备战算法最友好

你每天的目标明确：

选题 → 做题 → 测试 → 分类 → commit

极其简单，不会分心。

📈 4. GitHub 会成为你真正的技术作品

你最终会拥有一个这样结构的仓库：

leetcode-python/
  problems/
    array/
    dp/
    tree/
  templates/
  tools/
      sort_leetcode.py
      create_problem.py
      generate_readme.py
  tests/
  README.md



















```
每次写题后：

VS Code 自动生成 → problems/xxxx.py

你写完题目，运行脚本：

```python
python tools/sort_leetcode.py
```
自动移到：

problems/array/0001_two_sum.py

```shell
git add . && git commit -m "feat: add 0001 two sum"
```

推送到 GitHub。
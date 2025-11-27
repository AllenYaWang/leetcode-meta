import os
import sys
import datetime

TEMPLATE = """# -*- coding: utf-8 -*-
\"\"\"
LeetCode: {id}. {name}
Difficulty: {difficulty}
URL: https://leetcode.com/problems/{url}/

Approach:
1.
2.
3.

Time Complexity: O()
Space Complexity: O()
\"\"\"

from typing import *


class Solution:
    def solve(self, ...):
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve(...))
"""


def main():
    if len(sys.argv) < 4:
        print("Usage: python create_problem.py <id> <slug> <difficulty> <category>")
        return

    pid, slug, diff, cat = sys.argv[1:5]

    filename = f"{pid}_{slug}.py"
    path = f"problems/{cat}/{filename}"

    os.makedirs(f"problems/{cat}", exist_ok=True)

    with open(path, "w") as f:
        f.write(TEMPLATE.format(id=pid, name=slug.replace('_', ' ').title(), 
                                difficulty=diff.title(), url=slug))

    print(f"Created: {path}")


if __name__ == "__main__":
    main()

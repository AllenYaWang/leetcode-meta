#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = k - 1  # 第 k 大（降序）
        head, tail = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(head, tail)]

            # 三路划分
            left = head       # > pivot
            i = head        # current
            right = tail      # < pivot

            while i <= right:
                if nums[i] > pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                    i += 1
                elif nums[i] < pivot:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
                else:
                    i += 1

            # 现在区间是：
            # [head, left-1]   > pivot
            # [left, right]       == pivot
            # [right+1, tail]  < pivot

            if target < left:
                tail = left - 1
            elif target > right:
                head = right + 1
            else:
                return pivot


nums = [3,2,1,5,6,4]
k =2
solve = Solution()
print(solve.findKthLargest(nums, k))

# @lc code=end

'''
结合你的上述解法，这道题作为面试题会涉及哪些提问？
-----------------------------------------------------------------
很好，这个问题非常像真实面试的追问链路。我会严格结合你刚才遇到的 TLE 场景（大量重复元素 + 快速选择），
从面试官视角，系统地拆解这道题可能涉及的提问层次与考察点。
注：TLE 是 "Time Limit Exceeded" 的缩写，中文意思是“时间限制超时”。

一、第一层：基础理解（一定会问）
1️⃣ 你能说一下这道题的最优时间复杂度解法吗？

期望回答：

使用 快速选择（Quickselect）

平均时间复杂度 O(n)，空间复杂度 O(1)（原地）

👉 面试官在看你是否：

知道这不是必须排序

理解 Top-K 问题的本质

2️⃣ 为什么不用直接排序？

期望回答：

排序是 O(n log n)，而题目要求 O(n)

实际上只需要第 k 大，不需要完整有序

二、第二层：算法原理（重点）
3️⃣ 快速选择和快速排序有什么区别？

期望回答：

快速排序：两边都递归

快速选择：只递归一边（包含目标索引的一侧）

👉 面试官想确认你不是“背模板”。

4️⃣ pivot 是如何选择的？为什么要随机？

期望回答：

随机选择 pivot

避免退化成 O(n²)（如有序数组、全相等数组）

📌 这里已经埋下了你这次 TLE 的伏笔

三、第三层：致命测试用例（你刚刚踩中的坑）
5️⃣ 如果数组中有大量重复元素会发生什么？

这是一个高频追问

你这次的用例：

[1,1,1,1,1,1,1,1,1,1, ...]
k = 50000

面试官期待你意识到：

普通 二路 partition（< pivot / ≥ pivot）

pivot 每次几乎落在边界

问题规模几乎不缩小

退化成 O(n²) → 超时

👉 你这次 TLE 正是标准面试“陷阱用例”

四、第四层：关键改进（面试加分点）
6️⃣ 如何优化快速选择以应对大量重复元素？

正确答案：三路划分（Dutch National Flag）

划分为：

< pivot | == pivot | > pivot


然后：

如果 target 在 == pivot 区间 → 直接返回

否则只递归一侧

📌 面试官非常看重你能否主动提到三路划分

7️⃣ 为什么三路划分能避免超时？

期望解释：

一次 partition 可以“吃掉”大量等于 pivot 的元素

在全相等数组中，一轮就结束

复杂度从 O(n²) 降为 O(n)

五、第五层：工程 & 实战意识（高级面）
8️⃣ 递归实现有什么问题？

可答点：

递归深度最坏 O(n)

Python 可能栈溢出

可改为 while 循环

9️⃣ 如果你在面试中时间紧，你会选哪种方案？

这是一个现实型问题

合理回答：

Python：直接 heapq.nsmallest 或 nlargest

或 sorted(nums)[-k]

说明：工程中优先稳定可读，除非明确要求 O(n)

👉 面试官看的是取舍能力

六、横向对比追问（经常出现）
10 堆解法 vs 快速选择？
方法	时间复杂度	优点	缺点
小顶堆 (size k)	O(n log k)	稳定	非最优
快速选择	O(n) avg	最优	实现复杂
11 如果是数据流呢？

引出：

LeetCode 703

必须用堆，不能用 quickselect

七、终极总结（面试官真正想考什么）

这道题表面是 Top-K，实际上在考：

✅ 算法层面

快速选择原理

随机化思想

退化情况分析

✅ 工程层面

极端测试意识（你刚好遇到）

对 Python 性能边界的理解

✅ 思维层面

能否识别“理论最优 ≠ 实际最稳”

是否知道如何修补算法缺陷

最重要的一句话（送你）

“你能写出会 TLE 的 quickselect，说明你已经超过 70% 的人；
能解释为什么 TLE，并给出三路划分，说明你是面试通过级别。”

如果你愿意，下一步我可以帮你：

🎯 模拟一次完整面试对话

🧠 把这题扩展成 Top-K 模板总结

🧪 给你一组「专杀快排的测试用例合集」

你选哪个？
'''


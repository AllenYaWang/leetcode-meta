#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] Two Sum
#
# aproach:
# metho1: brute force
# t(n)= o(n^2)
# s(n)= o(1)
# method2: hashtable
# t(n)=o(n)
# s(n)=o(n)
# 
#
# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 边遍历，边存，边找
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [i, hashtable[target-num]]
            hashtable[num] = i
        return []
        

# summary
# conference: https://leetcode.cn/problems/two-sum/solutions/434597/liang-shu-zhi-he-by-leetcode-solution/?source=vscode
# 要有“ 边遍历，边存，边找” 的思想。


#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# approach: hashset
# o(n^2), o(n)
# @lc code=start
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort
        # special cases
        if not nums:
            return 0
        hashset = set(nums)
        logest =  1
        for num in hashset:
            if num-1 not in hashset:  # 神来之笔/extremely trim
                cnt = 1
                while num+1 in hashset:
                    cnt+=1
                    num+=1
                logest=max(logest, cnt)
        return logest

# ls = [-1,3, 5, 2, -2, 0, 1]
# s = Solution()
# print(s.longestConsecutive(ls))
      
# @lc code=end


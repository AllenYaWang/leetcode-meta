#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] Move Zeroes
#
# approch: 一次遍历 + o(n)空间
# t(n) = o(n), s(n)=o(n)
# @lc code=start
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # special cases
        if n <2:
            return nums
        res = []
        for i in range(n-1, -1, -1):
            if nums[i]==0:
                res.append(0)
            else:
                res.insert(0, nums[i])
        nums=deepcopy(res)
        print(res)
    



        
# @lc code=end


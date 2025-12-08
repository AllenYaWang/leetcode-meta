#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#
# 时间复杂度：O(n! * n)
# 空间复杂度：递归深度 O(n) + 结果 O(n! * n)
# backtracing = dfs + 状态撤销
# @lc code=start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        path = []

        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return res
    
# solve = Solution()
# print(solve.permute([1, 2, 3]))
        
# @lc code=end


#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] House Robber
#
# approach: dp
# （1）定义状态：for每个房间，只有两种可能，被偷 和 不被偷；
# dp[i]表示偷到第i个房间盗窃的最大值；
# （2） 递推关系【状态转移方程】：
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# （3）初始条件和边界值：
# dp[0]=nums[0],dp[1] = max(nums[0], nums[1])
# (3)递推顺序：自底向上
# t(N)=o(n), s(N)=o(n)
# @lc code=start

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 边界值
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        # 初始状态
        l = nums[0]
        r = max(nums[0], nums[1])
        # traverse + programming
        # 优化空间复杂度 o(n)-> o(1)
        for i in range(2, n):
            dp = max(r, l+nums[i])
            l = r
            r = dp
        return r

        
# @lc code=end


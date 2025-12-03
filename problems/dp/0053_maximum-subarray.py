#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] Maximum Subarray
#
# 1. brute-force
# t(N)=o(n^3), s(n)=o(1)
# 2. dp
# (1)状态定义；dp[i]表示以i结尾的最大连续子数组和；
# (2)递推关系【状态转移方程】
# dp[i] = max(dp[i-1]+ nums[i], nums[i])
# 用i把所有数都扫描一边，记录以i结尾的连续子串的最大值，对于任何一个数要么你参与结尾，要么自立门户，作为开头；
# t(N)=o(n), s(N)=o(n)
# 优化空间复杂度：由于每次只需要dp[i-1]的值，用一个变量只记录这个dp[i-1]的值，值随着遍历变动；
'''
动态规划中，每一步的状态并非都是最优解，这点是和 贪心 不同的。
'''
# （3）初始值和边界值：
# dp[0]=nums[0]
# (4)递归顺序： 自下而上
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 边界值
        n = len(nums)
        if n == 1:
            return nums[0]
        # 初始条件和边界值
        dp = nums[0]
        # traverse + programing
        res = nums[0]
        for i in range(1, n):
            dp = max(dp + nums[i], nums[i])
            res = max(res, dp)
        return res
    
        
# @lc code=end


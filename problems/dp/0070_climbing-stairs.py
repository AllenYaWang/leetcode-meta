#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] Climbing Stairs
#
# approach:
# 1. recursion 总是自顶向下的
# 最小重复子问题；
# 1: 1, f(1)
# 2: 1 + 1
#    2        f(2)
# 3: f(2)+f(1)
# t(N)=o(2^n), s(n)=o()
# 2. DP 与recursion相反，总是自下向上+memo
# 初始值：同上
# 递推关系（状态转移方程）： f(n)=f(n-1)+f(n-2)
# @lc code=start
# 
class Solution:
    def climbStairs(self, n: int) -> int:
        # 边界值
        if n<3:
            return n
        # 初始值
        dp = [0]*(n+1)
        dp[1], dp[2]= 1, 2
        # traverse + p
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# solve = Solution()
# print(solve.climbStairs(3))
# @lc code=end


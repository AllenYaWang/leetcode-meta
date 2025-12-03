#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# approach:
# 1. brute-force t(N)=o(n), s(N)=o(1)
# 2. 扩散法 —— double pointers t(N)=o(2n^2), s(N)=o(1)
'''
说明：在方法分析中，不能因为多了一种情况：如存在奇数回文串 和 偶数回文串 两种，
但这两种的核心方法【指针遍历和走势】是一致的，是可以汇合的。就轻言放弃了！
—— 无非就是需要多加个 if分支来判断！
'''
#3. dp 动态递推
# 最优子结构 dp[i][j-i]
# 状态转移方程【递推关系】dp[i-1][j]==true if dp[i][j-1]==true and s[i-1]==s[j]
# 初始状态： dp[i][j]=false
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # special cases
        if len(s)<2:
            return s
        # 初始状态
        n = len(s)
        ele = [False]
        dp = [ele * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # traverse and transform
        max_len, start = 1, 0
        for length in range(2, n+1):
            for i in range(n+1-length):
                if s[i]==s[i+length-1]:
                    # 偶数的初始状态要考虑其中
                    if length==2 or dp[i+1][i+length-2]:
                        dp[i][i+length-1] = True
                        max_len = length
                        start = i
        return s[start: start + max_len]

# s = 'cbbd'
# solve = Solution()
# print(solve.longestPalindrome(s))

# @lc code=end


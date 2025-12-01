#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] Add Strings
#
# approach: 模拟整数运算过程，逐位运算；
# o(n), s(N)=o(1)
# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # reverse
        num1 = num1[::-1]
        num2 = num2[::-1]
        # traverse
        n = max(len(num1), len(num2))
        digit1, digit2, carry = 0, 0, 0
        res = ""
        for i in range(n):
            # 类似 c++ , 选择语句写法；
            digit1 = int(num1[i]) if i<len(num1) else 0
            digit2 = int(num2[i]) if i<len(num2) else 0

            s = digit1 + digit2 + carry
            res = str(s%10) + res
            carry = s // 10
        if carry:
            res = str(carry) + res
        return res

# s = Solution()
# print(s.addStrings('111', '2345'))

# @lc code=end


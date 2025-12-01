#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] Valid Parentheses
#
# approach : one traverse + stack
# t(N)=o(n), s(N)=o(n)
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # trim 
        if len(s) & 1 ==1:
            return False
        # find pairs
        hashtable = {'}':'{',']':'[',')':'('}
        stack = []
        for i, ch in enumerate(s):
            if ch not in hashtable:
                stack.append(ch)
            else:
                if not stack or stack.pop(-1)!=hashtable[ch]:
                    return False
        return not stack

        
# @lc code=end


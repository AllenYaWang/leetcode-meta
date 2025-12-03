#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# approach:
# 1. python切片[双指针下的滑动窗口]+ hashset;
# t(n)=o(n), s(n)=o(n)
# @lc code=start
'''
当前代码存在的问题：
1. 双指针的滑动窗口没有充分利用，导致效率不高。 —— 滑动窗口的左指针没有在遇到重复字符时向右连续移动，而是每次只移动一位。
 —— 所有，这不算是真正的滑动窗口算法。
2. 使用了set来检查重复字符。 - - 这会导致每次检查都需要O(n)的时间复杂度。- 所有，时间复杂度不是O(n)，而是O(n^2)。
改进点：
1. 使用字典来记录字符的最新位置，这样可以在遇到重复字符时直接跳过到重复字符的下一个位置。
2. 通过维护一个滑动窗口的左指针和右指针，来确保每次都能找到最长的无重复子串。

另记：
理解 while --> 是需要重复的if 语句。
滑动窗口法 —— 特殊的双指针方法。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # traverse
        l = 0
        hashtable = dict()
        longest = 0
        cnt = 0
        for r in range(len(s)):
            if s[r] in hashtable and hashtable[s[r]]>l:
                l = hashtable[s[r]]+1
            hashtable[s[r]]=r
            cnt = r - l+1
            longest=max(cnt, longest)
        return longest


s = 'abcba'
solve = Solution()
print(solve.lengthOfLongestSubstring(s))
        
# @lc code=end


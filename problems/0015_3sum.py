#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 3Sum
#
# approach:
# method1: force-brute o(n^3), o(1) 
# method2: 排序和双指针
# t(n)= o(nlogn)+o(n^2)=o(n^2)
# s(n)= o(n)
# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        n = len(nums)
        # special cases
        if len(snums) < 3 or snums[0] >0 or snums[-1]<0:
            return []
        res = []
        for i, num in enumerate(snums):
            hashtable = set()
            target = -num
            j = n-1
            while j > i:
                if target - snums[j] in hashtable:
                    res.append([num, snums[j], target-snums[j]])
                hashtable.add(snums[j])
                j=j-1
        print(res)
        if res:
            sets = set()
            for ele in res:
                t = tuple(sorted(ele))
                if t not in sets:
                    sets.add(t)
            return [list(ele) for ele in sets]
        return []


# ls = [0, 0, 0, 0]  
# solve = Solution()
# print(solve.threeSum(ls))

                    
            

        
        
# @lc code=end


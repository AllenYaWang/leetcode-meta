#
# @lc app=leetcode.cn id=3591 lang=python3
#
# [3591] Check if Any Element Has Prime Frequency
#
'''
t(N)=o(2n*sqrt(n))
s(N)=o(n)
'''
from typing import List
import math
from collections import Counter

# @lc code=start
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # 判断质数
        def is_prime(num):
            # trim
            if num < 2:
                return False
            elif num in (2, 3):
                return True
            elif num & 1 ==0 or num%3==0:
                return False
            limit = math.isqrt(num)
            for i in range(3, limit+1, 2):
                if num % i ==0:
                    return False
            return True
        
        # count time
        hashtable = Counter(nums)
        return any([is_prime(num) for num in hashtable.values()])
            
# nums = [1,1,11,4,8,1]
# solve = Solution()
# print(solve.checkPrimeFrequency(nums))     
# @lc code=end




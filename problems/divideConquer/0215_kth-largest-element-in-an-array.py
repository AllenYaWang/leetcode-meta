#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 暴力解法
        nums.sort()
        return nums[-k]
        '''
        k = len(nums) - k  # 转换为第k小的数

        def quickselect(l, r):
            if l == r:
                return nums[l]

            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot = nums[r]

            # 分区：小于 pivot 放左边
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)

        return quickselect(0, len(nums) - 1)
'''
# s = [3,2,1,5,6,4]
# solve = Solution()
# print(solve.findKthLargest(s, 2))

# @lc code=end


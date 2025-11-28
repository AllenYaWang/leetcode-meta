#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 3Sum
#
# approach:
# method1: force-brute o(n^3), o(1) 
# method2: 排序+ 哈希表
# t(n)= o(nlogn)+o(n^2)=o(n^2)
# s(n)= o(n)
# method3: 排序+ 双指针；
# t(n) = o(n^2)
# s(n) = o(n)
# @lc code=start
'''
| 比较点    | 方法 2：哈希法                         | 方法 3：双指针（最优）         |
| ------ | -------------------------------- | -------------------- |
| 渐进复杂度  | O(n²)                            | O(n²)                |
| 常数因子   | **大**（哈希操作 + 结果存 set + tuple 转换） | **非常小**（仅加减、比较、指针移动） |
| 去重代价   | 重                                | 很轻（跳过相同元素）           |
| 能否剪枝   | 几乎不能                             | **大量剪枝**             |
| 内存访问模式 | 随机访问（慢）                          | 连续访问（快）              |
| 实际运行速度 | 明显较慢                             | **最快**               |
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # SORT
        nums.sort()
        # specail cases - trim
        n = len(nums)
        if n<3 or nums[0]>0 or nums[-1]<0:
            return []
        # one tranverse + double pointers
        res = []
        for i in range(n-2):
            l, r = i+1, n-1
            # trim
            if nums[i]>0:
                break
            # remove repeat
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s==0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return res
    

# ls = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
# ls =[-1,0,1,2,-1,-4]
# s = Solution()
# print(s.threeSum(ls))
# # [[-5,1,4],[-5,1,4],[-3,-1,4],[-3,0,3],[-2,-1,3],[-2,1,1],[-1,0,1],[-1,0,1],[0,0,0]]
    






                    
            

# [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]

        
# @lc code=end


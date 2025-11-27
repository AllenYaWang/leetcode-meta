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
        # 排序
        nums.sort()
        n = len(nums)
        # speical case - trim-减枝
        if nums[0] >0 or nums[-1]<0 or len(nums)<3:
            return []
        # traverse + double pointers
        res = []
        for i in range(n-2):
            # trim
            if nums[i]>0:
                return res    # return res, 不能是return []
            # remove repeat
            if i>0 and nums[i]==nums[i-1]:
                continue
            # left pointer
            l = i+1
            # right pointer
            r = n-1
            # move pointers
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s==0:
                    res.append([nums[i], nums[l], nums[r]])
                    # remove repeat -- 重复过程,并防止越界
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    # continue to move
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return res
    

# # ls = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
# ls =[0, 0, 0]
# s = Solution()
# print(s.threeSum(ls))
# # [[-5,1,4],[-5,1,4],[-3,-1,4],[-3,0,3],[-2,-1,3],[-2,1,1],[-1,0,1],[-1,0,1],[0,0,0]]
    






                    
            

        
        
# @lc code=end


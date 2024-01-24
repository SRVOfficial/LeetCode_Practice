# LeetCode Problem No: 136 (Single Number)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for num in nums:
            res = res ^ num

        return res
    

obj = Solution()
T1 = obj.singleNumber([2,2,1])
T2 = obj.singleNumber([4,1,2,1,2])
T3 = obj.singleNumber([1])

print(T1) # 1
print(T2) # 4
print(T3) # 1
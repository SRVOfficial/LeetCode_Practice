# LeetCode Problem No: 1 (Two Sum)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Method 2 (TC : O(n))
        hashmap = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in hashmap:
                return [hashmap[needed], i]
            hashmap[n] = i

        return []

       








        # Method 1 (TC : O(n2))
        # for i in range(len(nums)):
        #     d = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == d:
        #             return [i, j]
        
        # return []
    

obj = Solution()
T1 = obj.twoSum([2,7,11,15], 9)
T2 = obj.twoSum([3,2,4], 6)
T3 = obj.twoSum([3,3], 6)

print(T1) # [0,1]
print(T2) # [1,2]
print(T3) # [0,1]
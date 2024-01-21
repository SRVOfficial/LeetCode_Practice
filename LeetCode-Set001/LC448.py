# LeetCode Problem No: 448

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for num in nums: # TC : O(n)
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        return [i+1 for i, num in enumerate(nums) if num > 0] # TC : O(n) and SC : O(n) or O(1)
    
obj = Solution()
T1 = obj.findDisappearedNumbers([4,3,2,7,8,2,3,1])
T2 = obj.findDisappearedNumbers([1,1])
print(T1)
print(T2)

# Time Complexity : O(n)
# Space Complexity : 
    # A.) Worst Case (almost all the values are missing) -> O(n)
    # B.) Best Case (no missing values) -> O(1)
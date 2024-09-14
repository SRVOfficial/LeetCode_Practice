class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, size = 0, 0
        cur_max = 0

        for num in nums:
            if num > cur_max:
                cur_max = num
                res = 0
                size = 1
            elif num == cur_max:
                size += 1
            else:
                size = 0
            res = max(res, size)

        return res
            

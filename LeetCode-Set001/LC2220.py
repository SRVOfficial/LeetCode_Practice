class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        # Method 2
        n = start ^ goal
        while n:
            res += n & 1
            n = n >> 1
        return res




        # Method 1
        # while start or goal:
        #     # if (start % 2) != (goal % 2):
        #     if (start & 1) != (goal & 1):
        #         res += 1
            
        #     start //= 2
        #     goal //= 2
        
        # return res
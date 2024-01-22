# LeetCode Problem No: 1207 (Unique Number of Occurrences)

from typing import List


# Method 3
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counts = dict()
        for e in arr:
            counts[e] = counts.get(e, 0) + 1

        return len(set(counts.values())) == len(counts)
    




# Method 2
# from collections import Counter
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:

#         # count the occurrence of each item using Counter() function
#         counts = Counter(arr)  # give dictionary object

#         # check if the counts are unique
#         return len(set(counts.values())) == len(counts)




# Method 1
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:

#         arr.sort()
#         res = []
#         count = 0
#         for i in range(len(arr)):
#             if i == 0 or (i > 0 and arr[i] != arr[i-1]):
#                 if count in res:
#                     return False
#                 res.append(count)
#                 count = 1
#             else:
#                 count += 1
#         if count in res:
#             return False
#         return True
    



obj = Solution()
TC1 = obj.uniqueOccurrences([1,2,2,1,1,3])
TC2 = obj.uniqueOccurrences([1,2])
TC3 = obj.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(TC1)
print(TC2)
print(TC3)
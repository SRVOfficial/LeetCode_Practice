# LeetCode Problem No: 496 (Next Greater Element I)

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Method 2
        hashmap = {}
        for i, n in enumerate(nums1):
            hashmap[n] = i
        
        res = [-1]*len(nums1)

        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                res[hashmap[val]] = num

            if num in hashmap:
                stack.append(num)

        return res




        # Method 1
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         flag = False
        #         if nums2[j] == nums1[i]:
        #             for k in range(j+1, len(nums2)):
        #                 if nums2[k] > nums2[j]:
        #                     res.append(nums2[k])
        #                     flag = True
        #                     break
        #             else:
        #                 res.append(-1)
        #         else:
        #             if flag:
        #                 break                       

        # return res
    

obj = Solution()
T1 = obj.nextGreaterElement([4,1,2], [1,3,4,2])
T2 = obj.nextGreaterElement([2,4], [1,2,3,4])
T3 = obj.nextGreaterElement([4,1,2], [2,1,3,4])

print(T1) # [-1,3,-1]
print(T2) # [3,-1]
print(T3) # [-1,3,3]
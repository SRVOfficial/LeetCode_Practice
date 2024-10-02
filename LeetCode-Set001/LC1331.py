class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # sorted_list = sorted(set(arr))

        # hashmap = {num : rank+1 for rank, num in enumerate(sorted_list)}

        # return [hashmap[num] for num in arr]






        hashmap = {}

        sorted_arr = sorted(arr)

        r = 0
        for i, n in enumerate(sorted_arr):
            if i > 0 and n == sorted_arr[i-1]:
                pass
            else:
                r += 1
            hashmap[n] = r

        for i, n in enumerate(arr):
            arr[i] = hashmap[n]

        return arr

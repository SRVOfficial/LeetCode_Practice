class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i-1]
        
        # Process queries
        res = []
        for left, right in queries:
            # XOR of range [left, right] = prefix_xor[right+1] ^ prefix_xor[left]
            res.append(prefix_xor[right+1] ^ prefix_xor[left])
        
        return res
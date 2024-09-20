class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted_str = ""
        for e in s:
            converted_str += str(ord(e) - ord('a') + 1)

        
        for i in range(k):
            res = 0
            for n in converted_str:
                res += int(n)
            converted_str = str(res)

        return res
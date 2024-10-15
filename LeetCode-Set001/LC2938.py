class Solution:
    def minimumSteps(self, s: str) -> int:
        count_zero = 0
        res = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                count_zero += 1
            else:
                res += count_zero

        return res if res != 0 else 0
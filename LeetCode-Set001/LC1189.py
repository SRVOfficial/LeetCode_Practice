# LeetCode Problem No: 1189 (Maximum Number of Balloons)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        text_counter = {}
        balloon_counter = {}

        for e in text:
            text_counter[e] = text_counter.get(e, 0) + 1


        for e in "balloon":
            balloon_counter[e] = balloon_counter.get(e, 0) + 1


        res = len(text)
        for c in balloon_counter:
            if c in text_counter:
                res = min(res, text_counter[c] // balloon_counter[c])
            else:
                return 0
        return res
    

obj = Solution()
T1 = obj.maxNumberOfBalloons("nlaebolko")
T2 = obj.maxNumberOfBalloons("loonbalxballpoon")
T3 = obj.maxNumberOfBalloons("leetcode")
T4 = obj.maxNumberOfBalloons("lloo")

print(T1) # 1
print(T2) # 2
print(T3) # 0
print(T4) # 0

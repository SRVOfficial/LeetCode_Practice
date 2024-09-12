class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for e in s:
            hashmap[e] = hashmap.get(e, 0) + 1

        for i, e in enumerate(s):
            if hashmap[e] == 1:
                return i

        return -1
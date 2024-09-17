class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}

        for s in s1.split(" "):
            hashmap[s] = hashmap.get(s, 0) + 1

        for s in s2.split(" "):
            hashmap[s] = hashmap.get(s, 0) + 1

        return [s for s in hashmap if hashmap[s] == 1]
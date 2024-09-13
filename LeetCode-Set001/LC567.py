class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for e in s1:
            s1_count[e] = s1_count.get(e, 0) + 1

        window_count = {}
        
        for i in range(len(s2)):
            # add the current element in the window
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

            # if window size become bigger than the s1, remove the left element
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            # compare the window with s1_count
            if window_count == s1_count:
                return True

        return False
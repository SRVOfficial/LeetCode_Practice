class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_min(t):
            h, m = t.split(":")
            return int(h)*60 + int(m)

        timePoints = sorted([convert_to_min(t) for t in timePoints])

        timePoints.append(timePoints[0] + 1440)

        min_diff = float('inf')
        for i in range(1, len(timePoints)):
            min_diff = min(min_diff, timePoints[i] - timePoints[i - 1])

        return min_diff
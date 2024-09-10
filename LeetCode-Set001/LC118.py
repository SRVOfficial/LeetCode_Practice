class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows <= 0:
            return res 

        for i in range(numRows):
            
            temp = [1] * (i + 1)

            
            for j in range(1, i):
                temp[j] = res[-1][j - 1] + res[-1][j]

            res.append(temp)

        return res
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        

        res = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res.append(grid[i][j])

        while k >= len(grid)*len(grid[0]):
            k -= len(grid)*len(grid[0])
            
        res = res[len(res)-k::] + res[:len(res)-k]
        k = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = res[k]
                k += 1


        return grid
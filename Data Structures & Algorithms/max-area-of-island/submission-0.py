class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxSize = 0
        self.visit = set()
        self.count = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in self.visit or grid[i][j] == 0:
                print("first here")
                return

 
            self.count += 1
            self.visit.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.count = 0
                    dfs(row, col)
                    self.maxSize = max(self.count, self.maxSize)

        return self.maxSize
        
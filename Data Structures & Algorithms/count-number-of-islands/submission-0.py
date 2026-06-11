class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.numIslands = 0
        self.visit = set()
        def dfs(grid, i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return
            if grid[i][j] == "0" or (i, j) in self.visit:
                return

            if (i, j) not in self.visit:
                self.visit.add((i, j))
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visit:
                    self.numIslands += 1
                    dfs(grid, row, col)

        return self.numIslands
        
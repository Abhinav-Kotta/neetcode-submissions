from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        maxArea = 0
        area = 0

        def dfs(r, c):
            nonlocal area
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return

            area += 1
            grid[r][c] = 0
            for dx, dy in directions:
                dfs(r + dx, c + dy)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        count = 0

        def bfs(r, c):
            nonlocal maxArea
            directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            area = 0
            q = deque([(r, c)])
            grid[r][c] = 0

            while q:
                x, y = q.popleft()
                area += 1
                for dx, dy in directions:
                    nr, nc = x + dx, y + dy
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 0

            maxArea = max(maxArea, area)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    print(grid[r][c])
                    bfs(r, c)

        return maxArea
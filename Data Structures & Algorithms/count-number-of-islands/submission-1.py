from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque([(r, c)])
            directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            grid[r][c] = '0'
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nr, nc = x + dx, y + dy
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0':
                        continue
                    if grid[x + dx][y + dy] == '1':
                        q.append((nr, nc))

                    grid[nr][nc] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1

        return count
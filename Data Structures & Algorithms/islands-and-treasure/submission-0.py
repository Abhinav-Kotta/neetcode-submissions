from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]
        q = deque()
        visit = set()

        def addCell(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == -1:
                return

            visit.add((r, c))
            q.append([r, c])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visit.add((row, col))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r, c + 1)
                addCell(r, c - 1)
                addCell(r + 1, c)
                addCell(r - 1, c)
            dist += 1



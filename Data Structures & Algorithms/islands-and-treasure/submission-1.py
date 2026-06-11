from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r, c))

        def addCell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == -1:
                return

            q.append((r, c))
            visit.add((r, c))

        dist = 0
        while q:
            for nei in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dx, dy in directions:
                    addCell(r + dx, c + dy)

            dist += 1

                



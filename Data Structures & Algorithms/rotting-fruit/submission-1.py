class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visit = set()
        minutes = 0
        ripeOranges, currentRipe = 0, 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ripeOranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        def addCell(r, c):
            nonlocal currentRipe
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] != 1:
                return

            currentRipe += 1
            q.append((r, c))
            visit.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    addCell(r + dx, c + dy)
            minutes += 1

        if ripeOranges == 0:
            return 0
        elif ripeOranges != currentRipe:
            return -1
        else:
            return minutes - 1
        

            

        
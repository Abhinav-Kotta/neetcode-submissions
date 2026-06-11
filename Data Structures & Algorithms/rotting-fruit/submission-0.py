class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        ripeOranges = 0
        currentRipe = 0

        def addCell(r, c):
            nonlocal currentRipe
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return
            currentRipe += 1
            q.append([r, c])
            visit.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ripeOranges += 1
                if grid[row][col] == 2:
                    q.append([row, col])
                    visit.add((row, col))

        minutes = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            minutes += 1
        
        if ripeOranges == 0:
            return 0
        if currentRipe != ripeOranges:
            return -1
        else:
            return minutes - 1
        
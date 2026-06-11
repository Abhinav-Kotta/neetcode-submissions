class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight or (r, c) in visit:
                return

            visit.add((r, c))
            for dx, dy in directions:
                dfs(r + dx, c + dy, visit, heights[r][c])
            

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        return list(pac & atl)

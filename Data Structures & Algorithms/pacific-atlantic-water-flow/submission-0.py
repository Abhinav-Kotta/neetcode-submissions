class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, someSet, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in someSet or heights[r][c] < prevHeight:
                return

            someSet.add((r, c))
            dfs(r + 1, c, someSet, heights[r][c])
            dfs(r - 1, c, someSet, heights[r][c])
            dfs(r, c + 1, someSet, heights[r][c])
            dfs(r, c - 1, someSet, heights[r][c])


        for col in range(cols):
            dfs(0, col, pac, -1)
            dfs(rows - 1, col, atl, -1)

        for row in range(rows):
            dfs(row, 0, pac, -1)
            dfs(row, cols - 1, atl, -1)

        return [[row,col] for row,col in atl & pac]
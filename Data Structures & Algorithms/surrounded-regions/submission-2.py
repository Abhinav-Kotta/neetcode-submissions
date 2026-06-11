class Solution:
    def solve(self, board: List[List[str]]) -> None:
        badSet = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or (r, c) in badSet:
                return

            badSet.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in badSet:
                    board[row][col] = "X"
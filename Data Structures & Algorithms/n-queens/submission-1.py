class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]

        posDiag, negDiag, cols = set(), set(), set()

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                posDiag.add(row + col)
                negDiag.add(row - col)
                cols.add(col)
                board[row][col] = "Q"

                backtrack(row + 1)

                posDiag.remove(row + col)
                negDiag.remove(row - col)
                cols.remove(col)
                board[row][col] = "."

        backtrack(0)
        return res
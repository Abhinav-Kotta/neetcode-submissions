class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def backtrack(subset, r, c, i):
            if len(subset) == len(word):
                return True

            temp = board[r][c]
            board[r][c] = '#'

            for d in directions:
                x, y = r + d[0], c + d[1]
                if x >= 0 and x < rows and y >= 0 and y < cols:
                    if board[x][y] == word[i]:
                        subset.append(board[x][y])
                        if backtrack(subset, x, y, i + 1):
                            return True
                        subset.pop()
                
            board[r][c] = temp
            return False
            

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack([word[0]], row, col, 1):
                        return True


        return False
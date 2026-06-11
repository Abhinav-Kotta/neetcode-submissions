class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make a rowSet, colSet, boxSet
        # while adding to set, check if it's still unique
        # if not, return False
        # else return True at the end

        rowSet, colSet = defaultdict(set), defaultdict(set)
        boxes = [[set(), set(), set()] for _ in range(3)]
        print(boxes)
        rows = len(board[0])
        cols = len(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in boxes[r // 3][c // 3]:
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxes[r // 3][c // 3].add(board[r][c])

        return True
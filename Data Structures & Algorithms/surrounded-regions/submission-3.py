class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()
        badSet = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            if board[r][0] == 'O':
                badSet.add((r, 0))
                q.append((r, 0))
            if board[r][cols - 1] == 'O':
                badSet.add((r, cols - 1))
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                badSet.add((0, c))
                q.append((0, c))
            if board[rows - 1][c] == 'O':
                badSet.add((rows - 1, c))
                q.append((rows - 1, c))

        def addCell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or (r, c) in badSet:
                return

            badSet.add((r, c))
            q.append((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    addCell(r + dx, c + dy)
                

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in badSet:
                    board[r][c] = 'X'
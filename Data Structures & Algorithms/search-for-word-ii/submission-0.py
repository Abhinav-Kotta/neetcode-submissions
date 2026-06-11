class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWords(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWords(word)

        visit, res = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            for dx, dy in directions:
                x, y = r + dx, c + dy
                dfs(x, y, node, word)

            visit.remove((r, c))
            
        curr = self.root
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root, "")

        return list(res)

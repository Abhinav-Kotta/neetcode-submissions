# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    temp.append(node.val)

            if temp:
                res.append(temp[-1])

        return res
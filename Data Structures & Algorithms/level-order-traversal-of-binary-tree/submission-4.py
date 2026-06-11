# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            tmp = []
            level_size = len(q)
            for ele in range(level_size):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if tmp:
                res.append(tmp)

        return res


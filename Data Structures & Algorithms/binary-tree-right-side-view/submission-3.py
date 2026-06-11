# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # make a q
        # assign root
        # while q
        # get the length of q
        # pop element
        # if exists, append .right node to q

        q = deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            right = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)

            if right:
                res.append(right.val)

        return res
            
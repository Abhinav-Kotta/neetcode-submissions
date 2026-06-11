# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # make a queue
        # add all childs
        # pop queue and add to sublist
        res = []
        q = deque([root])
        while q:
            temp = []
            q_len = len(q)
            for items in range(q_len):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    temp.append(node.val)
            if temp:
                res.append(temp)

        return res

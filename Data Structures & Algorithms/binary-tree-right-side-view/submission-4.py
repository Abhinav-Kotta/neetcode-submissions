# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # initialize a queue
        # queue represents current layer of nodes
        # append the last node appended into the q to the res
        # return res

        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            rightMostnode = None
            for _ in range(len(q)):
                rightMostNode = q.popleft()
                if rightMostNode.left:
                    q.append(rightMostNode.left)
                if rightMostNode.right:
                    q.append(rightMostNode.right)

            res.append(rightMostNode.val)

        return res
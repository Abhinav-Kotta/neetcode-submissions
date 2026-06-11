# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        temp = []
        self.isValid = True

        def inOrder(root, minimum, maximum):
            if not root:
                return

            if not (root.val > minimum and root.val < maximum):
                self.isValid = False

            inOrder(root.left, minimum, root.val)
            inOrder(root.right, root.val, maximum)

        inOrder(root, float('-inf'), float('inf'))
        return self.isValid

        
        
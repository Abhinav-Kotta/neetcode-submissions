# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0

            countNodes = 0
            if root.val >= maxVal:
                countNodes = 1
            maxVal = max(maxVal, root.val)
            countNodes += dfs(root.left, maxVal)
            countNodes += dfs(root.right, maxVal)
            return countNodes

        return dfs(root, root.val)
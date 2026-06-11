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

            currentNodes = 0
            if root.val >= maxVal:
                currentNodes = 1

            maxVal = max(root.val, maxVal)
            currentNodes += dfs(root.left, maxVal)
            currentNodes += dfs(root.right, maxVal)

            return currentNodes

        return dfs(root, root.val)
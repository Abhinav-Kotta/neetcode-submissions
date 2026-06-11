# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs(root):
            if not root:
                return
            
            if self.sameTree(root, subRoot):
                self.res = True

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
            

    def sameTree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        else:
            return False

        
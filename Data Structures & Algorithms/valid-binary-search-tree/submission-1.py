# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        isValid = True

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            res.append(root.val)
            print(root.val)
            inOrder(root.right)

        inOrder(root)
        print(res)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False

        return True


        
        
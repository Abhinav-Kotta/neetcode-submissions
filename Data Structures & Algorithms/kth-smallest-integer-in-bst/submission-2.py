# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # first go left
        # increase count
        # if there is nothing to the left and we are less than count, go to the right

        self.count = 0
        self.smallest = 0
        self.k = k
        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            self.count += 1
            if self.count == self.k:
                self.smallest = root.val
                return
            inOrder(root.right)

        inOrder(root)
        return self.smallest

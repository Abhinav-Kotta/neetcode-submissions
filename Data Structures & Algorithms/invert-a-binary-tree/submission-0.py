# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #         - Initialize an empty stack
    # - Initialize an empty list to store visited nodes
    # - Add the node we would like to start our traversal from to the stack
    # - while the stack is not empty:
    #     - Pop the topmost node off the stack and store it in a variable, `current`
    #     - If the node is not already in the list of visited nodes:
    #         - Add `current` to the list of visited nodes
    #     - Loop through the current node's neighbors:
    #         - If the neighbor has not yet been visited
    #             - Push the neighbor onto the stack
    # - Return list of visited nodes

        if not root:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root


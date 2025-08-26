# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # global res variable
        self.diameter = 0

        # this method returns the height from node
        def dfs(node):
            if not node:
                return 0

            # compute the left and right branch recursively
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter
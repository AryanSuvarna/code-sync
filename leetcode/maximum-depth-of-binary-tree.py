# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS Solution
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            height_left = dfs(node.left)
            height_right = dfs(node.right)
            
            return max(height_left, height_right) + 1

        return dfs(root)
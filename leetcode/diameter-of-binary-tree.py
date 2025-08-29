# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        # this dfs method will be computing the height of the branches
        def dfs(node):
            if not node:
                return 0
            
            left_branch = dfs(node.left)
            right_branch = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left_branch + right_branch)

            return 1 + max(left_branch, right_branch)
        
        dfs(root)

        return self.max_diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(root):
            # base case
            if not root:
                return 0
            
            left_branch = dfs(root.left)
            right_branch = dfs(root.right)

            # see if we can update the longest path here
            self.longest_path = max(left_branch + right_branch, self.longest_path)

            # return the longer of the 2 paths since we're only concerned with the longest path
            return 1 + max(left_branch, right_branch)
        
        dfs(root)
        return self.longest_path
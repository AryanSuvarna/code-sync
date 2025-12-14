# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):
            # base case
            if not root:
                return True

            # root value has to be in between these 2 values
            if not (left < root.val < right):
                return False
            
            # make sure the left and right branches are valid as well
            left_branch = dfs(root.left, left, root.val)
            right_branch = dfs(root.right, root.val, right)

            return left_branch and right_branch
        
        return dfs(root, float("-inf"), float("inf"))
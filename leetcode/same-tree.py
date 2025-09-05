# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # returns True/False
        def dfs(root_1, root_2):
            if not root_1 and not root_2:
                return True
            if root_1 and root_2 and root_1.val == root_2.val:
                return (dfs(root_1.left, root_2.left) and dfs(root_1.right, root_2.right))
            return False               
        return dfs(p, q)
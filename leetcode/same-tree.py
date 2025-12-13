# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False
        
        left_branch = self.isSameTree(p.left, q.left)
        right_branch = self.isSameTree(p.right, q.right)

        return left_branch and right_branch
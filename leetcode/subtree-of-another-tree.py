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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases:
        if not subRoot: return True # no subroot
        if not root: return False # subroot but no root

        # check if subroot exists in root
        if self.isSameTree(root, subRoot):
            return True
        
        # if it doesn't, recursively call isSubtree on the left and right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
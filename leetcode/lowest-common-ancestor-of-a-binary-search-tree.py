# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root or not p or not q:
            return None
        
        # if largest value btwn p and q is smaller than root, this means that root cannot be their ancestor
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if smallest value btwn p and q is larger than root, this mean that root cannot be their ancestor
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # the current value is their lowest common ancestor
        else:
            return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        if root_1 and root_2 and root_1.val == root_2.val:
            return self.sameTree(root_1.left, root_2.left) and self.sameTree(root_1.right, root_2.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        # there is a subroot but no root
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
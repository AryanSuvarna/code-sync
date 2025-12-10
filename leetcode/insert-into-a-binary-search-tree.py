# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we will only insert as leaf nodes; not worrying about balancing

        # base case
        if not root:
            return TreeNode(val)
        
        # case 1: val should be placed on right side of root
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # case 2: val should be placed on left side of root
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
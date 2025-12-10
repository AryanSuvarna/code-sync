# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # case 1: val greater than root.val
        if val > root.val:
            return self.searchBST(root.right, val)
        # case 2: val lesser than root.val
        if val < root.val:
            return self.searchBST(root.left, val)
        # case 3: we found val
        return root
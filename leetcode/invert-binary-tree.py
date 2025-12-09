# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def dfs(node):
            node_left = node.left
            node_right = node.right

            if node_left:
                dfs(node_left)
            if node_right:
                dfs(node_right)
            
            node.left = node_right
            node.right = node_left
        
        dfs(root)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_path = 0
        
        def dfs(root):
            # base case: return 0 if null node (no length)
            if not root:
                return 0
            
            # calculate left and right branch lengths
            left_length = dfs(root.left)
            right_length = dfs(root.right)

            # update largest path if possible
            self.largest_path = max(self.largest_path, left_length + right_length)
            
            # return the length of the larger of the 2 paths
            # (we're only concerned with the longest path on either side of root)
            return 1 + max(left_length, right_length)

        dfs(root)
        return self.largest_path
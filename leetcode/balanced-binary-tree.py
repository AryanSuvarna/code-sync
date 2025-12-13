# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # base case
            if not root:
                return (0, True)
            
            # POST ORDER TRAVERSAL

            # calculate left and right branch
            left_height, left_status = dfs(root.left)
            right_height, right_status = dfs(root.right)

            # print(f"{root.val}, left={left_height}, right={right_height}")

            # check if heights differ more than 1 AND checks if any of the subbranches were already unbalanced
            if abs(left_height - right_height) > 1 or not left_status or not right_status:
                return (0, False)
            
            return (1 + max(left_height, right_height), True)

        return dfs(root)[1]
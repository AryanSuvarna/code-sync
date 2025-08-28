# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # use DFS here to calculate the height of the branches.
        # if the branches differ by more than 1 level, it is not balanced 
        def dfs(node):
            if not node:
                # we keep track of whether tree is balanced and send this info upstream
                return [True, 0]
            
            # calculate the height of each branch
            left_branch = dfs(node.left)
            right_branch = dfs(node.right)
            
            balanced = True
            if left_branch[0] and right_branch[0] and abs(left_branch[1] - right_branch[1]) <= 1:
                balanced = True
            else:
                balanced = False
            
            return [balanced, 1 + max(left_branch[1], right_branch[1])]
        
        res = dfs(root)
        return res[0]
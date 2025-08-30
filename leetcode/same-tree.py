# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root_1, root_2):
            if not root_1 and not root_2:
                return True
            # root_1 and root_2 structurally differ from each other somehow 
            elif not root_1 or not root_2:
                return False
            else:
                # compute their branches recursively
                left_branches = dfs(root_1.left, root_2.left)
                right_branches = dfs(root_1.right, root_2.right)

                # if the branches are the same, check the current values
                if left_branches and right_branches and root_1.val == root_2.val:
                    return True
                else:
                    return False
                
        return dfs(p, q)
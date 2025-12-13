# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # PRE ORDER DFS SOLUTION

        def dfs(root, greatestVal):
            good_nodes = 0
            # base case
            if not root:
                return 0
            
            # pre order: if the root val is greater than or equal to the greatest val we tracked, it is a good node
            if root.val >= greatestVal:
                good_nodes = 1
                greatestVal = root.val
            
            # recursive calculate good nodes on the left and right branch
            good_nodes += dfs(root.left, greatestVal)
            good_nodes += dfs(root.right, greatestVal)
            
            return good_nodes
            
        return dfs(root, root.val)
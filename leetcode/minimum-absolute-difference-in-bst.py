# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # In order traversal
        
        curr = root
        prev_node_val = float("-inf")
        min_diff = float("inf")
        # stores the nodes to visit in-order
        stack = []

        while curr or stack:
            # if node is not None, keep moving down the left branch
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                
                # calculate the diff between the curr and prev value
                min_diff = min(min_diff, abs(curr.val - prev_node_val))
                
                # update prev_node_val with the current node's value
                prev_node_val = curr.val
                
                # check the right side of the branch as well
                curr = curr.right
        
        return min_diff
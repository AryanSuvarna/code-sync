# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        stack = []
        prev = float("-inf")
        curr = root

        while curr or stack:
            # keep appending the left side of the tree
            if curr:
                stack.append(curr)
                curr = curr.left
            # once there is no left side, try to calculate the difference between any 2 parent-child relationship
            else:
                curr = stack.pop()
                min_diff = min(min_diff, abs(curr.val - prev))
                # update the prev value so we can compare with other branches of the tree. 
                prev = curr.val
                # check right side of the tree as well
                curr = curr.right

        return min_diff
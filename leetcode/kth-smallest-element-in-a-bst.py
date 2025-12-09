# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In order traversal solution
        
        curr = root
        count = 0
        # store the nodes in the order they are visited
        stack = []

        while curr or stack:
            # append all the left nodes first before we start counting to k
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop the most recent visited node and update count as we are processing this node 
            curr = stack.pop()
            count += 1

            # if count == k, return the current value
            if count == k:
                return curr.val
            
            # we need to process the right branch as well
            curr = curr.right
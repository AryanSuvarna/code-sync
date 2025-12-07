# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In order traversal
        stack = []
        n = 0
        curr = root

        while curr or stack:
            # keep going left and appending results till we cant no more
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            curr = curr.right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS

        if not root:
            return 0
        
        q = deque([(root, 1)])

        while q:
            curr, depth = q.popleft()

            # curr is a leaf node
            if not curr.left and not curr.right:
                return depth
            
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))
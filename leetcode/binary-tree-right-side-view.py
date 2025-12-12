# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS Solution
        
        # base case
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            # calculate number of nodes on this level
            num_nodes = len(q)

            for i in range(num_nodes):
                node = q.popleft()

                # if this node is the last node on this level, append to res
                if i == num_nodes - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
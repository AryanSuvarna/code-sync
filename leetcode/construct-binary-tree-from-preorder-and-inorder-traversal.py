# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursive solution

        # base case
        if not preorder or not inorder:
            return None
        
        # first element in preorder is always the root of the tree
        root = TreeNode(preorder[0])

        # find the middle of the inorder array. this tells us what elements are on left and right branch
        middle = inorder.index(preorder[0])

        # recursively build the tree with the left and right values or the tree
        root.left = self.buildTree(preorder[1 : middle + 1], inorder[ : middle])
        root.right = self.buildTree(preorder[middle + 1 : ], inorder[middle + 1: ])
    
        return root
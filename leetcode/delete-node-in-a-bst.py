# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # base case: cannot find node to delete
        if not root:
            return None
        
        # case 1: key is larger than root.val so search right branch
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # case 2: key is smaller than root.val so search left branch
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # case 3: we found node to delete
        else:
            # subcase 1: node to delete has 0 or 1 child
            # Note: this also works with the case where we delete a lead node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # subcase 2: node to delete has 2 children

            # we should update the node removed with the smallest value of the right
            # branch. This is done so that we gurantee that the node we pick is greater
            # than all nodes in the left branch and smaller than all nodes in the right
            # branch

            else:
                smallest = self.smallestNode(root.right)
                # update the current root val with the smallest val on right branch
                root.val = smallest.val
                # remove the smallest node now
                root.right = self.deleteNode(root.right, smallest.val)
        
        # return root after we have updated the BST
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base cases 
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # find middle of nums array and use this as the root of BST
        middle = math.ceil(len(nums) / 2)

        # create the node for the root
        root = TreeNode(nums[middle - 1])
        
        # create left and right arrays (not including root)
        left_half = nums[: middle - 1]
        right_half = nums[middle :]

        root.left = self.sortedArrayToBST(left_half)
        root.right = self.sortedArrayToBST(right_half)

        return root
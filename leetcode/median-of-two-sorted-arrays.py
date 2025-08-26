class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # very naive solution
        return median(sorted(nums1 + nums2))
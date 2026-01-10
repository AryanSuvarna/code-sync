class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # BOTTOM UP SOLUTION
        
        # dp array keeping track of the largest subsequence we can create at each index
        LIS = [1] * len(nums)

        # iterate backwards
        for i in range(len(nums) - 1, -1, -1):
            # check every position after index i
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # return the largest subsquence in the list
        return max(LIS)
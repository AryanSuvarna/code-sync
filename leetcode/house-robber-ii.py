class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1:
            return nums[0]

        # efficient DP solution (O(1) space complexity)
        def dp(arr):
            rob_1, rob_2 = 0, 0

            for num in arr:
                tmp = max(num + rob_1, rob_2)
                rob_1 = rob_2
                rob_2 = tmp
            
            return rob_2
        
        second_to_last = dp(nums[:-1])
        second_to_first = dp(nums[1:])

        return max(second_to_first, second_to_last)
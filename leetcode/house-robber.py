class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            # out of bounds
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(
                # rob current house
                nums[i] + dp(i + 2),
                # skip current house
                dp(i + 1)
            )

            return memo[i]
        
        return dp(0)
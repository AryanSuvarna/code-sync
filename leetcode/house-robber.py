class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            # 2 scenarios: rob or skip current house
            rob = nums[i] + dp(i + 2)
            skip = dp(i + 1)

            memo[i] = max(rob, skip)

            return memo[i]
        
        return dp(0)
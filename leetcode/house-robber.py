class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(n):
            # our of bounds case
            if n >= len(nums):
                return 0
            
            # we already cached max value from n
            if n in memo:
                return memo[n]
            
            # 2 cases: rob OR skip current house
            rob = nums[n] + dp(n + 2)
            skip = dp(n + 1)

            # take the max and return
            memo[n] = max(rob, skip)

            return memo[n]

        
        return dp(0)
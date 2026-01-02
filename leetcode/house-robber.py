class Solution:
    def rob(self, nums: List[int]) -> int:
        # memoize past computations
        memo = {}

        def dp(i):
            # base case: end of list
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            # rob the current house and go 2 houses down
            rob = nums[i] + dp(i + 2)

            # skip this house and go the next house
            skip = dp(i + 1)

            memo[i] = max(rob, skip)

            # return the scenario that returns the highest value
            return memo[i]
        
        res = dp(0)

        return res
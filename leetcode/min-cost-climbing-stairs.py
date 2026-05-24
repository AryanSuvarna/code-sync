class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            # case: out of bounds
            if i >= len(cost):
                return 0
            
            # case: check if we have already memoized position i
            if i in memo:
                return memo[i]
            
            # memoize the current position and return
            memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))

            return memo[i]

        return min(dp(0), dp(1))
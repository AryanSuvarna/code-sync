class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            # out of bounds error
            if i >= len(cost):
                return 0
            
            # current cost + cost from next step and 2 steps after
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]
        
        # take the min from step 0 or step 1
        return min(dfs(0), dfs(1))
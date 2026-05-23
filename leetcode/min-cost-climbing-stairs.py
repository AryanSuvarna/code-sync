class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            # out of bounds case
            if i >= len(cost):
                return 0
            
            # position i in cached in memo
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            
            return memo[i]

        return min(dfs(0), dfs(1))
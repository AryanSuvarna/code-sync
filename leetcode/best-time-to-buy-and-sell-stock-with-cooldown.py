class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DFS

        # dp dictionary to memoize already calculated solution
        # key = (idx, buying), value = max_profit
        dp = {}

        def dfs(i, buying):
            # base case: out of bounds
            if i >= len(prices):
                return 0
            # base case: already memoized
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # buying or selling
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # key = (idx, buy/sell), val = max_profit
        dp = {}

        def dfs(idx, buying):
            # out of bounds case
            if idx >= len(prices):
                return 0
            # we already cached this value
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            
            # cases where we buying or selling the stock
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx] 
                cooldown = dfs(idx + 1, buying)
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, not buying) + prices[idx] 
                cooldown = dfs(idx + 1, buying)
                dp[(idx, buying)] = max(sell, cooldown)
            
            return dp[(idx, buying)]

        return dfs(0, True)
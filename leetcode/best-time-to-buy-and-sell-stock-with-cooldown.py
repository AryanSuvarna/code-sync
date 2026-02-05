class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this cache will store the results of buying/selling at specific indices
        # key = (idx, will_buy) val = max_profit
        dp = {}

        def dfs(i, will_buy):
            # base case: out of bounds
            if i >= len(prices):
                return 0
            # we've already computed the max profit when buying/selling at this idx
            if (i, will_buy) in dp:
                return dp[(i, will_buy)]
            
            if will_buy:
                # if we buy, we cannot buy anymore. we must change state to sell
                buy = dfs(i + 1, not will_buy) - prices[i]
                cooldown = dfs(i + 1, will_buy)
                dp[(i, will_buy)] = max(buy, cooldown)
            else:
                # if we sell, change it back to buying state (negation)
                sell = dfs(i + 2, not will_buy) + prices[i]
                cooldown = dfs(i + 1, will_buy)
                dp[(i, will_buy)] = max(sell, cooldown)
            
            return dp[(i, will_buy)]
        
        return dfs(0, True)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max_profit = 0, 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
        
        return max_profit
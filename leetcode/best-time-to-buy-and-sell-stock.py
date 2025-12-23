class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        
        for r in range(1, len(prices)):
            diff = prices[r] - prices[l]

            profit = max(profit, diff)

            if prices[l] > prices[r]:
                l = r
            
        return profit
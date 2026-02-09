class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp 2d array for keeping track of combos
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        coins.sort()

        # set the amount = 0 column to 1 bc there is only one combo to get amount = 0
        for r in range(n + 1):
            dp[r][0] = 1
        
        for c in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                if a >= coins[c]:
                    # case where we skip curr coin
                    dp[c][a] = dp[c + 1][a]
                    # case where we also include current coin
                    dp[c][a] += dp[c][a - coins[c]]
        
        return dp[0][amount]
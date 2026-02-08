class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # set all positions with amount = 0 to 1 (only 1 way to get 0)
        for i in range(n + 1):
            dp[i][0] = 1

        # bottom up: build solution
        for i in range(n - 1, -1, -1):
            # start at 1, since we already know values in a = 0
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    # skip curr coin
                    dp[i][a] = dp[i + 1][a]
                    # use curr coin
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]
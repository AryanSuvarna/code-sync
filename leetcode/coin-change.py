class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        memo = {}

        def dp(total):
            # total was already computed before
            if total in memo:
                return memo[total]
            # we reached total
            if total == 0:
                return 0
            # we overshot
            if total < 0:
                return float("inf")
            

            res = float("inf")
            for coin in coins:
                # res here computes the number of coins needed
                res = min(res, 1 + dp(total - coin))
            
            memo[total] = res
            return memo[total]
        
        ans = dp(amount)
        return -1 if ans == float("inf") else ans
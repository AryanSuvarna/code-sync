class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # simple base case; early exit
        if amount == 0:
            return 0
        
        # dp memoization, store min coins needed for each result
        memo = {}

        def dp(total):
            # total in memo
            if total in memo:
                return memo[total]
            # we can get to total
            if total == 0:
                return 0
            # we overshot
            if total < 0:
                return float("inf")
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1 + dp(total - coin))
            
            memo[total] = res

            return res
        
        ans = dp(amount)

        return -1 if ans == float("inf") else ans
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            # base case
            if i <= 2:
                return i
            
            # check if in memo
            if i in memo:
                return memo[i]
            
            # cache result and return
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)
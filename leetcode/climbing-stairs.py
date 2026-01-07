class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(step):
            # check if we have already memoized this step
            if step in memo:
                return memo[step]
            
            # base cases 
            if step <= 2:
                return step
            
            # recurrence relation
            memo[step] = dp(step - 1) + dp(step - 2)

            return memo[step]
        
        return dp(n)
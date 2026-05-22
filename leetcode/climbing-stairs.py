class Solution:
    def climbStairs(self, n: int) -> int:
        # TOP DOWN DP APPROACH
        
        def dp(n, cache):
            # for values (0,1,2,3), the # of ways to climb stairs is just the value
            if n < 4:
                return n
            # if in the cache, return wtv value we already calculated
            if n in cache:
                return cache[n]
            
            # store the value in the cache before returning
            cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
            return cache[n]
        
        return dp(n, {})
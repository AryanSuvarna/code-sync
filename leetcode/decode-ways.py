class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        # dp array; base case is that we'e reached the end of the string so we have found a way to decode
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)

            if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            
            dp[i] = res
            
            return dp[i]
        
        return dfs(0)
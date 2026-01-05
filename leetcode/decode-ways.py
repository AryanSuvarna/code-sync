class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            # single digit
            res = dfs(i + 1)
            
            # double digit
            if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)
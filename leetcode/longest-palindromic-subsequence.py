class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # BOTTOM UP DP SOLUTION

        # 2D array
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]

        s_reversed = s[::-1]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                # same value
                if s[i] == s_reversed[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # different value
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
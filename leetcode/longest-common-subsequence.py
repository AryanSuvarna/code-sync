class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a dp 2d array that will act as a cache
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # case where the letters match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # get the largest of the right or bottom position from curr
                # do this to keep track of common letter as we build solution 
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
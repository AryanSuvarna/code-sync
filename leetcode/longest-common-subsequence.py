class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # BOTTOM UP APPROACH
        
        # create a 2d DP array that will track the LCS in each subproblem
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # iterate backwards since we are building it bottom up
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # same character case
                if text1[i] == text2[j]:
                    # take the sum of the value that is on the diagonal of curr pos
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        # return the first position since we're buidlding bottom up
        return dp[0][0]
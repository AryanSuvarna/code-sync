class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # BOTTOM UP DP SOLUTION
        
        # 2D array for DP problem
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # same value
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                # different values
                else:
                    # take the larger of the right or bottom dp value
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        # return the first value
        return dp[0][0]
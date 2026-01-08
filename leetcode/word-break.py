class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BOTTOM UP APPROACH

        # our DP array
        dp = [False for i in range(len(s) + 1)]

        # base case: if we ever reach the end of the string, we have successfully broken strings
        dp[len(s)] = True
    
        for i in range(len(s) - 1, -1, -1):
            # checking if from ith index, we can create one of the words
            for word in wordDict:
                # check if the word can be made starting for index i
                if s[i : i + len(word)] == word:
                    # if possible, use the subproblems we already solved to determine if word can be segmented
                    dp[i] = dp[i + len(word)]
                # break early if we already found a suitable word
                if dp[i]:
                    break
        
        # print(dp)
        return dp[0]
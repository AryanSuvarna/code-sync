class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TOP DOWN APPROACH
        # create a memo array
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            # we've reached the end bottom left corner
            if r == m - 1 and c == n - 1:
                return 1
            # out of bounds case
            if r >= m or c >= n:
                return 0
            # we already have this value memoized
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[r][c]
        
        return dfs(0, 0)
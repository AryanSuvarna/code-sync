class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        # DFS function
        def dfs(r, c, visited, prev_height):
            # edge cases: visited cell, boundary cases, curr cell is smaller than previous
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev_height:
                return
            
            # run dfs from this cell if passing all edge cases
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        for c in range(COLS):
            # run dfs on first row, which is touching the pacific ocean
            dfs(0, c, pac, heights[0][c])
            # run dfs on last row, which is touching the atlantic ocean
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # run dfs on first column, which is touching pacific
            dfs(r, 0, pac, heights[r][0])
            # run dfs on last column, which is touching atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        # get intersection of both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        
        return res
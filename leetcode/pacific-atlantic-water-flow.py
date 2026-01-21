class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c , visited, prev_height):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev_height > heights[r][c] or (r, c) in visited:
                return
            
            # run dfs on all directions if current cell is a valid cell
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        # first we start with the rows
        for c in range(COLS):
            # run dfs on the first row as all cells are touching the pac. ocean
            dfs(0, c, pac, heights[0][c])

            # run dfs on last row as all cells are touching the atl. ocean
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        # now the columns
        for r in range(ROWS):
            # run dfs on first col as all cells are touching pac. ocean
            dfs(r, 0, pac, heights[r][0])

            # run dfs on last col as all cells are touching atl. ocean
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        # get the intersection of both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        
        return res
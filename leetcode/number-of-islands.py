class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # check edge cases
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            # if we dont pass any of the edge cases, then the curr position is land
            # we will set it to 0 to mark it as "visited" (we never look at 0 spots ever)
            grid[r][c] = "0"

            # search grid now in all 4 directions
            for x, y in directions:
                dfs(r + x, c + y)
    
        # go thru every position till we see land. once we do, run dfs on that position
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count
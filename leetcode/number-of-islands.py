class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(row, col):
            # edge cases 
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return
            
            # change land to water so we dont visit it ever again 
            grid[row][col] = '0'
            
            # check in all directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return

        numIslands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    numIslands += 1
        
        return numIslands
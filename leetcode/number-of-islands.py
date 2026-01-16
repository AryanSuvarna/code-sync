class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # dfs solution
        def dfs(r, c):
            # edge cases (boundaries) and we're on water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            # mark curr position as visited by changing it to a water
            grid[r][c] = "0"

            # run dfs on all 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        island_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # run dfs to find whole island and mark it as visited
                    dfs(r, c)
                    island_count += 1
        
        return island_count
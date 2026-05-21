class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or grid[r][c] == "0":
                return
            
            # mark the current cell as water so we dont visit again
            grid[r][c] = "0"
            
            # run dfs in every direction
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        island_count = 0

        # double for loop to go thru every cell val and find land
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if we are at land, we run dfs to find the whole island and mark as visited
                if grid[r][c] == "1":
                    dfs(r, c)
                    island_count += 1

        return island_count
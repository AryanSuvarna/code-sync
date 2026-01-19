class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # queue will be needed to perform BFS
        q = deque()
        fresh_count = 0
        time_count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def rot_orange(r, c):
            nonlocal fresh_count
            # our of bounds edge case and case where 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            
            # we have fresh orange, so rot it and add rotten orange to queue
            grid[r][c] = 2
            q.append([r, c])
            fresh_count -= 1
            

        # we find all oranges, rotten and fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # go thru the queue
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    rot_orange(r + dr, c + dc)
            
            time_count += 1

        return time_count if fresh_count == 0 else -1
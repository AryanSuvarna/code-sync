class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            #  if cell is out of bounds, return False
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 
            if board[r][c] != 'O':
                return
            
            # if we find a 'O' cell that is connected to the border, we mark that as B for boundary cell and try to see if there is more cells like this that is connected
            board[r][c] = 'B'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # find all 'O' cells that are connected to border and then run dfs
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        

        # now we mark all 'O' as 'X' and the 'B' cells get set back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'
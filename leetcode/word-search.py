class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        cells_visited = set()

        def backtrack(row, col, word_length):
            # base case: we found a word
            if len(word) == word_length:
                return True
            
            # boundary cases, visited case and letter mismatch case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in cells_visited or word[word_length] != board[row][col]:
                return False
            
            cells_visited.add((row,col))

            # now check every direction
            up    = backtrack(row - 1, col, word_length + 1)
            down  = backtrack(row + 1, col, word_length + 1)
            left  = backtrack(row, col - 1, word_length + 1)
            right = backtrack(row, col + 1, word_length + 1)

            cells_visited.remove((row,col))

            return (up or down or left or right)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    res = backtrack(row, col, 0)

                    if res:
                        return True
        
        return False
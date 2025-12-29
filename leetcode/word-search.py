class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        cells_visited = set()

        # backtracking
        def backtrack(row, col, word_length):
            # base case: we found the word
            if word_length == len(word):
                return True
            
            # cases checking out of bounds AND if the current board piece is not part of word AND we havent visited this cell already
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or board[row][col] != word[word_length] or (row, col) in cells_visited:
                return False
            
            cells_visited.add((row, col))
            
            # now run dfs in all 4 directions
            down  = backtrack(row + 1, col, word_length + 1)
            up    = backtrack(row - 1, col, word_length + 1)
            left  = backtrack(row, col - 1, word_length + 1)
            right = backtrack(row, col + 1, word_length + 1)

            cells_visited.remove((row, col))

            return (left or right or up or down)


        # keep iterating on board until we reach the start of the word
        for row in range(len(board)):
            for col in range(len(board[0])):
                # we found start. perform backtrack to see if we can find word
                if board[row][col] == word[0]:
                    res = backtrack(row, col, 0)

                    if res:
                        return True
        
        # we didnt find start so word doesnt exist
        return False
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # SPACE OPTIMIZED SOLUTION

        # this represents the last row intially.
        row = [1] * n

        # go thru every row one by one and build answer (bottom up).
        # iterate till (m - 1) because we skip last row since we know its just 1s 
        for r in range(m - 1):
            # just set it to [1] because last column is always going to be 1
            new_row = [1] * n

            # iterate backwards on the columns
            for c in range(n - 2, -1, -1):
                new_row[c] = new_row[c + 1] + row[c]
            
            # update the row to new_row
            row = new_row
    
        # return first value of updated row as this represents pos. (0, 0)
        return row[0]
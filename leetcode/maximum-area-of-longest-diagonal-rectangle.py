class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        largest_diagonal_sq, largest_area = 0, 0

        # go thru each rectangle and compute diagonal
        for length, width in dimensions:
            # compute diagonal
            diagonal_sq = length * length + width * width
            area = length * width

            if diagonal_sq > largest_diagonal_sq:
                largest_diagonal_sq = diagonal_sq
                largest_area = area
            elif diagonal_sq == largest_diagonal_sq:
                largest_area = max(largest_area, area)
        
        return largest_area
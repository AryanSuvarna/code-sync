class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first, we determine which is a possible row that target can reside in
        left_row, right_row = 0, len(matrix) - 1
        m_row = 0

        while left_row <= right_row:
            m_row = (left_row + right_row) // 2

            if matrix[m_row][0] > target:
                right_row = m_row - 1
            elif matrix[m_row][-1] < target:
                left_row = m_row + 1
            else:
                break
        
        # check how we broke out of the while loop:
        if left_row > right_row:
            return False
        
        # now that we found a suitable row, we check if this row contains target
        row_to_check = matrix[m_row]
        l, r = 0, len(row_to_check) - 1

        while l <= r:
            m = (l + r) // 2

            if target == row_to_check[m]:
                return True
            elif target < row_to_check[m]:
                r = m - 1
            else:
                l = m + 1
        
        return False
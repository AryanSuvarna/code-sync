class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1
        m_row = l_row

        # find ideal row for target
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2

            if matrix[m_row][0] > target:
                r_row = m_row - 1
            elif matrix[m_row][-1] < target:
                l_row = m_row + 1
            else:
                break
        
        # return False if no ideal row is found for the target
        if not (l_row <= r_row):
            return False
        
        l, r = 0, len(matrix[m_row]) - 1

        # regular binary search
        while l <= r:
            m = (l + r) // 2

            if matrix[m_row][m] < target:
                l = m + 1
            elif matrix[m_row][m] > target:
                r = m - 1
            else:
                return True
        
        return False
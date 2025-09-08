class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # just go thru every combo of A and B that add up to n
        for A in range(1, n):
            B = n - A
            # check if A and B dont have a 0
            if "0" not in str(A) and "0" not in str(B):
                return [A, B]
        # no combos possible where A and B dont have zeroes
        return []
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # base case
        if n == 0:
            return [0]
        
        res = []
        # append increasing natural numbers up until n
        for i in range(1, n):
           res.append(i)
        
        # the last value is to append the sum of the res array multiplied by -1 to set sum to 0
        res.append(-1 * sum(res))

        return res
class Solution:
    def climbStairs(self, n: int) -> int:
        # BOTTOM UP APPROACH (build upwards from base cases)

        # base case
        one, two = 1, 1
        
        # iterate till i = n
        i = 2
        while i <= n:
            next_step = one + two
            # swap one_step with curr, and two_step with one
            one, two = next_step, one
            i += 1

        return one
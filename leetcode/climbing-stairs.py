class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up DP solution
        
        # init
        one_step, two_step = 1, 1
        curr = 0

        # iterate backwards from n -2 all the way to 0
        for _ in range(n - 2, -1, -1):
            curr = one_step + two_step
            # shift one_step and two_step to the left by 1
            one_step, two_step = curr, one_step
        
        # return the value at one_step as that contains the total # of ways from 0 to n
        return one_step
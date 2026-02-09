class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # key = (idx, sum), value = num_combos
        dp = {}

        def backtrack(idx, curr_sum):
            # base case: we already memoized this solution
            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]

            # base case: we used all the values
            if idx == len(nums):
                return 1 if curr_sum == target else 0
            
            # memoize this combo
            dp[(idx, curr_sum)] = (
                # count number of ways from 
                backtrack(idx + 1, curr_sum + nums[idx]) + 
                backtrack(idx + 1, curr_sum - nums[idx])
            )

            return dp[(idx, curr_sum)]
        
        return backtrack(0, 0)
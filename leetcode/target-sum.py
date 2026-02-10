class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # defaultdict(int): this will represent the sum-count pairs (key=sum, value=count)
        dp = defaultdict(int)

        # base case
        # this is saying that with 0 elements and a sum of 0, there is one way to compute this
        dp[0] = 1

        # go thru every every index in nums
        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                # move to the next row and add the curr nums value
                next_dp[cur_sum + nums[i]] += count
                # move to the next row and remove the 
                next_dp[cur_sum - nums[i]] += count
            
            # reassign for next loop 
            dp = next_dp

        # we're looking for the value that is stored at when we use all the indices and we reached the target value
        return dp[target]
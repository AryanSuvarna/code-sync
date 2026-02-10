class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # defaultdict(int): this will represent the sum-count pairs (key=sum, value=count)
        dp = [defaultdict(int) for i in range(len(nums) + 1)]

        # base case
        # this is saying that with 0 elements and a sum of 0, there is one way to compute this
        dp[0][0] = 1

        # go thru every every index in nums
        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                # move to the next row and add the curr nums value
                dp[i + 1][cur_sum + nums[i]] += count
                # move to the next row and remove the 
                dp[i + 1][cur_sum - nums[i]] += count

        # we're looking for the value that is stored at when we use all the indices and we reached the target value
        return dp[len(nums)][target]
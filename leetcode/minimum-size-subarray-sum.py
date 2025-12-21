class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # do this so we know that res did not get updated
        res = len(nums) + 1
        rolling_sum, l = 0, 0

        for r in range(len(nums)):
            rolling_sum += nums[r]

            while rolling_sum >= target:
                res = min(res, r - l + 1)
                rolling_sum -= nums[l]
                l += 1
        
        # res did not get updated so no subarray exists
        if res == len(nums) + 1:
            return 0
        # otherwise return res
        else:
            return res
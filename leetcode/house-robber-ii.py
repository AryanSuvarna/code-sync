class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        if len(nums) == 1:
            return nums[0]
        
        # DP function
        def dp(i, arr):
            if i >= len(arr):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(arr[i] + dp(i + 2, arr), dp(i + 1, arr))

            return memo[i]
        
        # run DP solution on nums array up until 2nd last element
        second_last = dp(0, nums[:-1])

        memo.clear()

        # run DP solution on nums array from 2nd element to end
        print(nums[1:])
        second_first = dp(0, nums[1:])

        # return the largest of the 2
        return max(second_last, second_first)
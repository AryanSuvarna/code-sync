class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        # edge case
        if len(nums) == 1:
            return nums[0]


        def dp(i, arr):
            # out of bounds case
            if i >= len(arr):
                return 0
            
            # cached result
            if i in memo:
                return memo[i]
            
            # cached result
            memo[i] = max(arr[i] + dp(i + 2, arr), dp(i + 1, arr))

            return memo[i]

        # nums arr [0: n - 1]
        first = dp(0, nums[:-1])
        memo.clear()

        # nums arr [1: ]
        second = dp(0, nums[1:])

        return max(first, second)
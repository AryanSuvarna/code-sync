class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            # base case: index is out of bounds
            if i >= len(nums):
                return 0
            
            # check if we've already computed the largest robbing value from index i
            if i in memo:
                return memo[i]
            
            # 2 scenarios: rob house i and move on OR skip house i and check next
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            # take the larger of the 2 options and memoize it
            memo[i] = max(rob, skip)

            return memo[i]
        
        res = dfs(0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr_subset = []
        def backtrack(idx):
            # base case: index is out of bounds. append whatever we have on subset to res
            if idx >= len(nums):
                # append a copy since the subset is potentially going to be modified later
                res.append(curr_subset.copy())
                return
            
            # decision we take to include current index value
            curr_subset.append(nums[idx])
            backtrack(idx + 1)

            # decision we take to NOT include current index value
            curr_subset.pop()
            backtrack(idx + 1)
        
        backtrack(0)
        return res
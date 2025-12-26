class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.add(tuple(subset))
                return
                
            # include
            subset.append(nums[i])
            backtrack(i + 1)

            # exclude
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        nums.sort()
        backtrack(0)
        return [list(l) for l in res]
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, subset):
            if i >= len(nums):
                res.add(tuple(subset))
                return

            # decision 1 (include): append curr idx value
            subset.append(nums[i])
            backtrack(i + 1, subset)
            
            # decision 2 (exclude): pop curr idx
            subset.pop()
            # if the next element is the same as the current, we skip it (we've already processed it and created every unique subset)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]
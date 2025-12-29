class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            # include
            total += candidates[i]
            subset.append(candidates[i])
            
            # explore
            backtrack(i, total)

            # exclude
            total -= candidates[i]
            subset.pop()

            # explore next value
            backtrack(i + 1, total)
            
        backtrack(0, 0)
        return res
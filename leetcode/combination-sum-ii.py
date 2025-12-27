class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # include curr indx
            total += candidates[i]
            subset.append(candidates[i])
            backtrack(i + 1, total)

            # exclude curr idx
            total -= candidates[i]
            subset.pop()
            # skip duplicate numbers since we already processed this value above
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)

        # candidates list must be sorted so we can avoid dupes
        candidates.sort()
        backtrack(0,0)
        return res
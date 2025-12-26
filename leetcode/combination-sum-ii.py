class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            res = []

            curr_combo = []

            def backtrack(i, total):
                if total == target:
                    res.append(curr_combo.copy())
                    return
                if total > target or i >= len(candidates):
                    return
                
                total += candidates[i]
                curr_combo.append(candidates[i])
                backtrack(i + 1, total)

                total -= candidates[i]
                curr_combo.pop()
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                backtrack(i + 1, total)

            candidates.sort()
            backtrack(0,0)
            return res
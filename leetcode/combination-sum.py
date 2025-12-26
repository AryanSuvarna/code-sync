class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curr_combo = []

        def backtrack(idx, total):
            if total > target or idx >= len(candidates):
                return
            elif total == target:
                res.append(curr_combo.copy())
                return

            total += candidates[idx]
            curr_combo.append(candidates[idx])
            backtrack(idx, total)

            total -= candidates[idx]
            curr_combo.pop()
            backtrack(idx + 1, total)
        
        backtrack(0, 0)

        return res
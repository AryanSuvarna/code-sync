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
            
            # keep adding current idx value to total to get as close to target as possible
            total += candidates[idx]
            curr_combo.append(candidates[idx])
            backtrack(idx, total)

            # now we remove the current value and see if we can append the next value
            total -= candidates[idx]
            curr_combo.pop()
            backtrack(idx + 1, total)
        
        backtrack(0, 0)
        return res
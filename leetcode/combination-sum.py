class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(combo.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                
                combo.append(candidates[j])
                backtrack(j, total + candidates[j])
                combo.pop()
            
        backtrack(0, 0)
        return res
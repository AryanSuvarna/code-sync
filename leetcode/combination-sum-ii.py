class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        path = []
        def backtrack(curr_idx, total):
            if total == target:
                res.append(path.copy())
                return
            
            for i in range(curr_idx, len(candidates)):
                # we've seen this value already
                if i > curr_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # early break if the candidate value will be greater than target
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                path.pop()
        
        backtrack(0, 0)
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(num_used):
            # base case: we made a permutation
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for num in nums:
                if num in num_used:
                    continue
                
                # add
                subset.append(num)
                num_used.add(num)
                
                # explore
                backtrack(num_used)

                # remove
                subset.pop()
                num_used.remove(num)
        
        backtrack(set())

        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(num_used, perm):
            # base case: we made a permutation!
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for num in nums:
                # skip this num as it's in permutation already
                if num in num_used:
                    continue
                
                # include num
                num_used.add(num)
                perm.append(num)

                # explore with new addition...
                backtrack(num_used, perm)

                # exclude
                num_used.remove(num)
                perm.pop()
            
        backtrack(set(), [])

        return res
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        # create a map for the number count
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1

        def backtrack(perm):
            # base case: we've built a permutation!
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for num in num_map:
                if num_map[num] > 0:
                    # add num in perm
                    perm.append(num)
                    num_map[num] -= 1
                    
                    # explore...
                    backtrack(perm)

                    # remove this value
                    perm.pop()
                    num_map[num] += 1

        backtrack([])
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # RECURSIVE SOLUTION
        # base case
        if len(nums) == 0:
            return [[]]
        
        # self calling self.permute till you get to base case and build upwards
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            # add the element that you excluded (nums[0]), to every possible position (start, middles, end)
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res
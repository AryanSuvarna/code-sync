class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0

        for n in nums:
            tmp = max(rob_2, rob_1 + n)
            rob_1, rob_2 = rob_2, tmp
        
        return rob_2
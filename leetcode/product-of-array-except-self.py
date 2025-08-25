class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prod = 1
        for i in range(len(nums)):
            ans[i] = prod 
            prod *= nums[i]
        
        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= prod
            prod *= nums[j]
        
        return ans
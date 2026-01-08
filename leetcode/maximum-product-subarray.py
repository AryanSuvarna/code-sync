class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) operation
        res = max(nums)

        max_prod, min_prod = 1, 1

        for num in nums:
            # multiplying anything by 0 is 0. so we reset the max and min prod variables here
            if num == 0:
                max_prod, min_prod = 1, 1
                continue
            
            # calculate the max and min product values. this way is done so that we take care of negative values
            old_max_prod = max_prod
            max_prod = max(num * max_prod, num * min_prod, num)
            min_prod = min(num * old_max_prod, num * min_prod, num)

            res = max(max_prod, res)
        
        return res
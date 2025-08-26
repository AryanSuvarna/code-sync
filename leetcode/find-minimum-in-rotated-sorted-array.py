class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search
        l, r = 0, len(nums) - 1
        smallest = nums[l]

        while l <= r:
            # sublist already sorted
            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break
            
            m = (l + r) // 2
            smallest = min(smallest, nums[m]) # update smallest before making any checks
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return smallest
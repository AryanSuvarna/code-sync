class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # determine which side of list nums[m] is in
            # this will help us to quickly find target

            # left side is sorted, so we search the left side if target present
            if nums[m] > nums[r]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            # right side is sorted, so we search right side if target present
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
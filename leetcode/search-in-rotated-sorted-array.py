class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # problem running in O(log n) is clear indicating that binary search is needed for problem

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            # we found target!
            if target == nums[m]:
                return m

            # we're on left side of split
            if nums[r] < nums[m]:
                # within range of (l, m)
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            # we're on right side of split
            else:
                # within range of (m, r)
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
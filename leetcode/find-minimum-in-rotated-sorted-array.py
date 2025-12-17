class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[l]

        while l <= r:
            print(smallest)
            # edge case: the list is already sorted or a single element in list
            if nums[l] <= nums[r]:
                smallest = min(smallest, nums[l])
                return smallest

            # update smallest variable with middle value if possible
            m = (l + r) // 2
            smallest = min(smallest, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return smallest
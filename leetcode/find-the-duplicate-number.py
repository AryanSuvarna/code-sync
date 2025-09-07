class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the first intersection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # if they are at same index, break out of loop
            if slow == fast:
                break

        # find 2nd intersection. This intersection gurantees the duplicate value
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow
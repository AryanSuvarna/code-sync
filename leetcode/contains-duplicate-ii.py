class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            # window greater than k
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            # we found duplicate in window
            if nums[r] in window:
                return True
            
            # add this value otherwise
            window.add(nums[r])

        return False
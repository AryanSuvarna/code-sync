class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init variables
        l, r = 0, 0
        output = []
        # we will store the indices here; easier to know what elements to remove when shifting window
        # this queue will also store the max values
        q = collections.deque() 

        # go thru each window
        while r < len(nums):
            # check if curr value is max in queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # check if the max needs to be popped if its index is out of range of window
            while q[0] < l:
                q.popleft()

            # if window is size k, add max to output. also update window
            if (r - l + 1) == k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output
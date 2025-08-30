class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices, values are in decreasing order (monotonic decreasing)
        l = r = 0

        while r < len(nums):
            # pop smaller values from the back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove leftmost index if it's out of the window
            if q[0] < l:
                q.popleft()

            # record the max value once the first window is formed
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1  # move window forward

            r += 1

        return output
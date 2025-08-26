class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min speed is one banana; max speed is eating largest pile in 1 hr
        l, r = 1, max(piles)
        k = l

        # try to find minimum k such that Koko will be able to finish all bananas before guards come back
        while l <= r:
            m = (l + r) // 2

            # compute how long it will take to eat all piles with rate of m
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / m)
            
            if time_taken > h:
                l = m + 1
            else: # check if we can find a smaller minimum
                k, r = m, m - 1
        
        return k
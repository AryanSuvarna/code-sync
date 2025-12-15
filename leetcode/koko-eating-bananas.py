class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is our right bound (should only eat at rate of largest pile)
        largest_pile = max(piles)

        l, r = 1, largest_pile
        min_rate = largest_pile

        while l <= r:
            rate = (l + r) // 2
            
            # calculate total time taken for rate
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / rate)

            if time_taken > h:
                l = rate + 1
            else:
                # update min rate if possible with a smaller rate
                min_rate = min(min_rate, rate)
                r = rate - 1
        
        return min_rate
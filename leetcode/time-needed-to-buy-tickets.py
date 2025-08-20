class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        
        for idx, tickets_needed in enumerate(tickets):
            if idx <= k:
                time_taken += min(tickets[k], tickets_needed)
            else:
                time_taken += min(tickets_needed, tickets[k] - 1)

        return time_taken
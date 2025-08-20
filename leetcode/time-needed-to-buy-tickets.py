class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        # before k
        for i in range(k):
            time_taken += min(tickets[k], tickets[i])
        # at k
        time_taken += tickets[k]
        
        # after k
        for j in range(k + 1, len(tickets)):
            if tickets[k] > tickets[j]:
                time_taken += tickets[j]
            else:
                time_taken += tickets[k] - 1
        return time_taken
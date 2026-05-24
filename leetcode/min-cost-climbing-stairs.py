class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # first example in desc: [10, 15, 20, 0]
        cost.append(0)

        # update the cost function directly to get the cost from position i
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(  
                cost[i] + cost[i + 1],
                cost[i] + cost[i + 2]
            )

        # return the first or second step (index 0 or 1), whichever has the smallest val
        return min(cost[0], cost[1])
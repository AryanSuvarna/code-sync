class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # append 0 to end of list to represent the top of the floor
        cost.append(0)

        # start at 3rd rightmost val because we know the last value will remain the same
        for i in range(len(cost) - 3, -1, -1):
            # take the min of curr value with 1 step and curr value with 2 steps and update the position
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        # cost[0] and cost[1] will be updated with the costs to get to top of the floor from position 0 and 1
        return min(cost[0], cost[1])
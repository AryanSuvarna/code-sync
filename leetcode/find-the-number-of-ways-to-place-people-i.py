class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x asc, then y desc
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0

        for i in range(len(points)):
            yi = points[i][1]
            maxY = float("-inf")
            # Explore candidate Bs
            for j in range(i + 1, len(points)):
                yj = points[j][1]
                # Condition: A is upper-left (yi >= yj)
                # And ensure no point has been inside rectangle: yj > maxY
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj

        return ans
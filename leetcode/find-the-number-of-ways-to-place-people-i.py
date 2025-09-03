class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x asc, then y desc
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0

        for a in range(len(points)):
            A_y = points[a][1]
            prev = float("-inf")
            # Explore candidate Bs
            for b in range(a + 1, len(points)):
                B_y = points[b][1]
                # Condition: A is upper-left (yi >= yj)
                # And ensure no point has been inside rectangle: yj > maxY
                if A_y >= B_y > prev:
                    ans += 1
                    prev = B_y

        return ans
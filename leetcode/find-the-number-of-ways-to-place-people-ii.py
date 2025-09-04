class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda p:(p[0], -p[1]))
        count = 0

        for a in range(len(sorted_points)):
            A_y = sorted_points[a][1]
            prev = float("-inf")
            for b in range(a + 1, len(sorted_points)):
                B_y = sorted_points[b][1]

                if A_y >= B_y > prev:
                    count += 1
                    prev = B_y

        return count
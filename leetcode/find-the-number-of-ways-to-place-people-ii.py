class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort the points
        sorted_points = sorted(points, key=lambda p:(p[0], -p[1]))
        count = 0

        for a in range(len(sorted_points)):
            # grab Alice's y coord
            A_y = sorted_points[a][1]
            prev = float("-inf")
            for b in range(a + 1, len(sorted_points)):
                # grab Bob's y coord
                B_y = sorted_points[b][1]

                # if Alice's and Bob's y-coord is greater than prev, this means there is no person in between them
                if A_y >= B_y > prev:
                    count += 1
                    prev = B_y

        return count
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # helper method to calcualte the gain in passing ratio
        def calculate_gain(num_passes, num_total):
            prev_ratio = num_passes / num_total
            new_ratio = (num_passes + 1) / (num_total + 1)
            return new_ratio - prev_ratio

        # for this problem, it makes sense to use a max heap that will always keep track of the max gain in passing ratio
        max_heap = []

        # calculate gain when adding a student to every class and add to heap
        for num_pass, num_total in classes:
            gain = calculate_gain(num_pass, num_total)
            max_heap.append((-gain, num_pass, num_total))

        # heapify!
        heapq.heapify(max_heap)

        # now go thru the heap and choose best spot for extra students
        for _ in range(extraStudents):
            # we only want to pop from the heap and add a student to the class that has the highest gain potential 
            gain, num_passes, num_total = heapq.heappop(max_heap)

            # put the same class back into the heap with an extra student while also calculating the gain
            # this will auto adjust the heap with the highest gain at the top always
            heapq.heappush(
                max_heap,
                (
                    -1 * calculate_gain(num_passes + 1, num_total + 1),
                    num_passes + 1,
                    num_total + 1,
                )
            )
        
        # calcualte the average pass ratio
        sum_avg_pass_ratio = sum(
            passes / total for _, passes, total in max_heap
        )

        return sum_avg_pass_ratio / len(classes)
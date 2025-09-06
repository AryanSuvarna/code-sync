class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        
        def get_operations(x):
            bits = 1
            base = 1
            total_ops = 0

            while base <= x:
                # operations required = (total amount of numbers you can make with bits) * (# of ops required to transform each number with x bits to 0)
                total_ops += (min(base * 2 - 1, x) - base + 1) * ((bits + 1) // 2)
                bits += 1
                base *= 2
            return total_ops
        
        # go thru every query
        for l, r in queries:
            # calculate the number of operations required for each interval
            res += (get_operations(r) - get_operations(l - 1) + 1) // 2
        
        return res
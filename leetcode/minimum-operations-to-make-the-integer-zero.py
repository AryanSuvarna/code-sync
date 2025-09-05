class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # basically we want this: num1 - k(2^i + num2) = 0, where k is the number of operations performed
        # OR: num1 = k(2^i) + k*num2
        # OR: num1 - k*num2 = 2^(sum of i)
        k = 1
        while True:
            x = num1 - k * num2

            # there is no way of getting a sum of x in k sum of powers of 2
            # ex. k = 7, x = 5. smallest power of 2 is 1 (2^0 = 1) and we have to do 7 times, which is 
            # impossible to be less than 5
            if x < k:
                return -1

            # if x >= k AND k meets the minimum number of sum powers needed to get x
            if k >= x.bit_count(): # counts the number of 1s in binary rep. of x
                return k
            k += 1
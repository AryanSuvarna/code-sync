class Solution:
    def maxDifference(self, s: str) -> int:
        letterCount = defaultdict(int)

        for letter in s:
            letterCount[letter] += 1
        
        maxOdd, minEven = -1, 10000

        for num in letterCount.values():
            if num % 2 == 0:
                minEven = min(minEven, num)
            else:
                maxOdd = max(maxOdd, num)
        
        return maxOdd - minEven
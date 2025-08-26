class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_jewels = 0
        # make jewels into a set for faster lookup
        jewel_set = set(jewels)

        for stone in stones:
            if stone in jewel_set:
                num_jewels += 1
        
        return num_jewels
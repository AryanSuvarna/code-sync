class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        letter_count = defaultdict(int)

        for r in range(len(s)):
            # append the new char to letter count first
            letter_count[s[r]] += 1
            
            # check if this is true: (window_size - largest_count > k)
            while (r - l + 1) - max(letter_count.values()) > k:
                letter_count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
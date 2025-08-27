class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest = 0, 0
        rolling_hash = defaultdict(int)

        most_frequent_letter_count = 0

        # use sliding window technique
        for r in range(len(s)):
            rolling_hash[s[r]] += 1
            # when we expand our window size, we try to update most_frequent_letter_count
            most_frequent_letter_count = max(most_frequent_letter_count, rolling_hash[s[r]])

            # check if window is too large to make k replacements with most frequent letter
            while (r - l + 1) - most_frequent_letter_count > k:
                rolling_hash[s[l]] -= 1
                l += 1
            # get the longest substring length, if possible 
            longest = max(longest, r - l + 1)
        
        return longest
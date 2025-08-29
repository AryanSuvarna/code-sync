class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize these variables
        l, longest, most_frequent_character = 0, 0, 0
        letter_map = defaultdict(int)

        for r in range(len(s)):
            # append the new character to map
            letter_map[s[r]] += 1
            # update the most_frequent_character only when we increase the window size
            most_frequent_character = max(most_frequent_character, letter_map[s[r]])

            # valid window: window length - most_frequent <= k
            while (r - l + 1) - most_frequent_character > k:
                letter_map[s[l]] -= 1
                l += 1
            
            # update the count of longest window, if possible
            longest = max(longest, r - l + 1)
        
        return longest
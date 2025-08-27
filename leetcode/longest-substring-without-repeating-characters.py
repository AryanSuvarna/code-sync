class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        letter_set = set()

        for r in range(len(s)):
            while s[r] in letter_set:
                letter_set.remove(s[l])
                l += 1
            letter_set.add(s[r])
            longest = max(longest, len(letter_set))
        return longest
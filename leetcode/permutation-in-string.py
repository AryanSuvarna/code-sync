class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation cannot exist is len(s1) is greater than len(s2)
        if len(s1) > len(s2):
            return False
        
        # get the letter hash map for s1
        s1_map = defaultdict(int)

        for c in s1:
            s1_map[c] += 1

        window_size = len(s1)
        l = 0
        s2_map = defaultdict(int)

        for r in range(len(s2)):
            # check if window is too large
            if (r - l + 1) > window_size:
                s2_map[s2[l]] -= 1
                # pop this if the count is 0 ever
                if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l])
                l += 1

            # append rightmost value
            s2_map[s2[r]] += 1

            # check if the maps are the same values
            if s2_map == s1_map:
                return True

        return False
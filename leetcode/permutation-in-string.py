class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 has to be larger than s1
        if len(s1) > len(s2):
            return False
        
        # get the letter count of s1 and get the window size
        s1_map = defaultdict(int)
        for ch in s1:
            s1_map[ch] += 1

        s1_window_size = len(s1)

        # lets initialize the rolling window
        l = 0
        s2_map = defaultdict(int)

        for i in range(s1_window_size):
            s2_map[s2[i]] += 1

        # now go thru each window in s2 until we have a match
        for r in range(s1_window_size, len(s2)):
            if s1_map == s2_map:
                return True
            
            # update the window if the 2 hashes aren't the same
            s2_map[s2[r]] += 1

            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                s2_map.pop(s2[l])
            l += 1
        
        # make one final check to see if the last updated window is a permutation
        return s2_map == s1_map
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "": return ""

        # initialize some variables
        res = [-1,-1]
        min_substring_length = float("inf")
        have = 0 # how many constraints for letters do i have
        t_map, window_map = defaultdict(int), defaultdict(int)

        # get the freq count of letters in t
        for ch in t:
            t_map[ch] += 1
        
        need = len(t_map) # how many constraints for letters I need to fulfill

        l = 0
        for r in range(len(s)):
            window_map[s[r]] += 1

            if s[r] in t_map and window_map[s[r]] == t_map[s[r]]:
                have += 1
            
            # try to find min window substring
            while have == need:
                # check if substring smaller than previously saved valid substrings
                if (r - l + 1) < min_substring_length:
                    res = [l, r]
                    min_substring_length = r - l + 1
                
                # make window smaller
                window_map[s[l]] -= 1
                if s[l] in t_map and window_map[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1
        
        # return answer
        left, right = res
        if min_substring_length != float("inf"):
            return s[left : right + 1]
        else:
            return ""
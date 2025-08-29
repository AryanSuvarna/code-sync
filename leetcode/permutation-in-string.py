class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # length of s2 cannot be less than length of s1
        if len(s2) < len(s1):
            return False
        
        # get the letter count of s1
        s1_map = defaultdict(int)

        for i in range(len(s1)):
            s1_map[s1[i]] += 1

        window_size = len(s1) 

        # initialize the rolling hash map of s2
        s2_map = defaultdict(int)

        for j in range(window_size):
            s2_map[s2[j]] += 1

        # then we are going to compare the 2 maps by having a sliding window with len(s1) size
        l = 0

        for r in range(window_size, len(s2)):
            if s2_map == s1_map:
                return True
            
            # add the next element
            s2_map[s2[r]] += 1

            # remove the left element
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                s2_map.pop(s2[l])
            l += 1
    
        return s1_map == s2_map
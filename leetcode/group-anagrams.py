class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this will store all words that have the same letter counts
        res = defaultdict(list)

        for word in strs:
            # store the letter count of each word and use that as the key to dict
            letter_count = [0] * 26

            for ch in word:
                letter_count[ord(ch) - ord('a')] += 1
            
            tuple_letter_count = tuple(letter_count)
            res[tuple_letter_count].append(word)
        
        return list(res.values())
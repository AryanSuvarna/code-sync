class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        res = []
        combo = ""

        def backtrack(i):
            nonlocal combo

            if i == len(digits):
                res.append(combo)
                return
        
            letters = num_to_letter[digits[i]]

            for letter in letters:
                combo += letter
                backtrack(i + 1)
                combo = combo[:-1]
        
        backtrack(0)
        return res
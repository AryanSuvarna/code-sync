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

        def backtrack(i, combo):
            # base case: we reached end of digits
            if i == len(digits):
                res.append(combo)
                return

            # get the possibe letters for the current digit
            letters = num_to_letter[digits[i]]

            # run backtrack on each letter
            for letter in letters:
                backtrack(i + 1, combo + letter)
        
        if digits:
            backtrack(0, "")
        
        return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(l_count, r_count, path):
            # base case: we have 3 pairs of parentheses
            if l_count == r_count == n:
                res.append(path)
                return
            
            # add left bracket if count is less than n
            if l_count < n:
                path += "("
                backtrack(l_count + 1, r_count, path)
                path = path[:-1]
            
            # add right bracket if count is less than the count of left brackets
            # we have to do this to ensure the parentheses remain valid
            if r_count < l_count:
                path += ")"
                backtrack(l_count, r_count + 1, path)
                path = path[:-1]
        
        backtrack(0, 0, "")
        return res
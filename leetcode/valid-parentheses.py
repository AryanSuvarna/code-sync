class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack = []
        for i in range(len(s)):
            if s[i] not in paren_map:
                stack.append(s[i])
            else:
                if stack and paren_map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
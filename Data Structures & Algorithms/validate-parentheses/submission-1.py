class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        parenthesis_mapping = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for i in range(0,len(s)):
            if s[i] in parenthesis_mapping:
                if(stack and parenthesis_mapping[s[i]] == stack[-1]):
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(s[i])
        if(len(stack) == 0):
            return True
        return False
            
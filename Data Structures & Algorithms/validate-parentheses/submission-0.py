class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        parenthesis_mapping = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for i in range(0,len(s)):
            try:
                if(len(stack) == 0):
                    stack.append(s[i])
                elif(parenthesis_mapping[s[i]] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    stack.append(s[i])
            except: 
                stack.append(s[i])
        if(len(stack) == 0):
            return True
        return False
            
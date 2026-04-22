class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_s = ''.join(filter(str.isalnum, s)).lower()
        for i in range(0,len(refined_s)//2):
            if(refined_s[i] == refined_s[len(refined_s) - i - 1]):
                continue
            else:
                return False
        return True
        
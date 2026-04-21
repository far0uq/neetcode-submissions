class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            letters = []
            for letter in s:
                letters.append(letter)
            for letter in t:
                try:
                    letters.remove(letter)
                except:
                    return False
        if(len(letters) == 0):
            return True
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            try:
                s_dict[letter] = s_dict[letter] + 1
            except:
                s_dict[letter] = 1
        for letter in t:
            try:
                t_dict[letter] = t_dict[letter] + 1
            except: 
                t_dict[letter] = 1
        if(s_dict == t_dict):
            return True
        return False
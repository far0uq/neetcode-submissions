class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_one = {}
        dict_two = {}

        if(len(s) != len(t)):
            return False
        else:
            for x in range(0, len(s)):
                print()
                try:
                    dict_one.update({s[x]:dict_one[s[x]] + 1})
                except:
                    dict_one[s[x]] = 1
                try:
                    dict_two.update({t[x]:dict_two[t[x]] + 1})
                except: 
                    dict_two[t[x]] = 1
        print(dict_one)
        print(dict_two)
        if(dict_one == dict_two):
            return True
        return False
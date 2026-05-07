from collections import OrderedDict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_representation = {}
        for string in strs:
            hashmap = {}
            for letter in string:
                hashmap[letter] = 1 + hashmap.get(letter,0)
            ordered_hashmap = OrderedDict(sorted(hashmap.items(), key=lambda item: item[0]))
            try:
                hashmap_representation[str(ordered_hashmap)].append(string)
            except:
                hashmap_representation[str(ordered_hashmap)] = []
                hashmap_representation[str(ordered_hashmap)].append(string)
        res = []
        for values in hashmap_representation.values():
            res.append(values)
        return res        
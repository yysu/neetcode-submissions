from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            char_list = [0] * 26
            for char in string:
                char_list[ord(char) - ord('a')] += 1

            res[tuple(char_list)].append(string)
        return list(res.values())    
                

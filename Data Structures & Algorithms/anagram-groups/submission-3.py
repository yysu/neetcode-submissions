from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            char_list = [0] * 26
            for char in s:
                char_list[ord(char) - ord('a')] += 1
            res[tuple(char_list)].append(s)
        
        return list(res.values())

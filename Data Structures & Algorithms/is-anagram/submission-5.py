class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict = {}
        for char in s:
            if char not in str_dict:
                str_dict[char] = 1
            else: 
                str_dict[char] += 1
        
        for char in t:
            if char not in str_dict:
                return False
            else:
                str_dict[char] -= 1
                if str_dict[char] == 0:
                    del str_dict[char]
        return len(str_dict) == 0

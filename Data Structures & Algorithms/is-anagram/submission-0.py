class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
        
        for char in t:
            if char not in char_dict:
                return False
            char_dict[char] -= 1
            if char_dict[char] == 0:
                del char_dict[char]
        
        if char_dict:
            return False
        return True
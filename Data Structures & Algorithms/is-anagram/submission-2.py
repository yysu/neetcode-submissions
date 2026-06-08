class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] == 0:
                    del char_dict[char]
            else:
                return False
        return len(char_dict) == 0
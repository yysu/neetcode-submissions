class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charTable = {}
        for char in s:
            if char not in charTable:
                charTable[char] = 1
            else:
                charTable[char] += 1
        
        for char in t:
            if char in charTable:
                charTable[char] -= 1
                if charTable[char] == 0:
                    del charTable[char]
            else:
                return False
        
        return len(charTable) == 0
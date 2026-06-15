class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
    
    def is_valid(self, char):
        return char.isalpha() or char.isdigit()
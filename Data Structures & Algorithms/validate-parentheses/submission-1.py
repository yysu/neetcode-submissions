class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if stack:
                    pop_char = stack.pop()
                    if mapping[char] != pop_char:
                        return False
                else:
                    return False
         
        return len(stack) == 0
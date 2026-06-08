class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if stack:
                    pop_char = stack.pop()
                    if pop_char != mapping[char]:
                        return False
                else:
                    return False

        return len(stack) == 0
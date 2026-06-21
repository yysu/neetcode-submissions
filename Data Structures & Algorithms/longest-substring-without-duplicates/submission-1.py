class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0

        numSet = set()
        while right < len(s):
            while s[right] in numSet:
                numSet.remove(s[left])
                left += 1
            
            numSet.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        return longest

            




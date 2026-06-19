class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, num in enumerate(nums):
            if target - num in hashTable:
                return [hashTable[target - num], i]
            else:
                hashTable[num] = i
                
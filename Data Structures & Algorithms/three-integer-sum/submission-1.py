class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index in range(len(nums)):
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            
            left, right = index + 1, len(nums) - 1
            last_pair = None
            while left < right:
                if nums[left] + nums[right] == -nums[index]:
                    if (nums[left], nums[right]) != last_pair:
                        result.append((nums[index], nums[left], nums[right]))
                    last_pair = (nums[left], nums[right])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[index]:
                    left += 1
                else:
                    right -= 1
        return result
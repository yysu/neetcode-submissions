class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index in range(len(nums)):
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            
            last_pair = None
            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[index]:
                    if (nums[left], nums[right]) != last_pair:
                        res.append([nums[index], nums[left], nums[right]])
                    last_pair = (nums[left], nums[right])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -nums[index]:
                    right -= 1
                else:
                    left += 1
        return res
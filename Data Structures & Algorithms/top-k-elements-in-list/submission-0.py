class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequent = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            frequent[cnt].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in frequent[i]:
                res.append(num)
                if len(res) == k:
                    return res
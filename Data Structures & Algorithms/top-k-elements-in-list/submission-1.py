from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqs = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freqs[cnt].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for freq in freqs[i]:
                res.append(freq)
                if len(res) == k:
                    return res
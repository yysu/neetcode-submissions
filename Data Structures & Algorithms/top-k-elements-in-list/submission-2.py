from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)

        for num, count in counts.items():
            freqs[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
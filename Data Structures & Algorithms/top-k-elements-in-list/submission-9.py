from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        return list(sorted(a,key=lambda x: a[x]))[-k:]

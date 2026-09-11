class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount=defaultdict(int)
      
        for i in nums:
            numcount[i]+=1
        return sorted(numcount,key=lambda x:numcount[x],reverse=True)[:k]
            
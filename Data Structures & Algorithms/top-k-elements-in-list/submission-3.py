class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount=defaultdict(int)
      
        for i in nums:
            numcount[i]+=1
        finalv=list(numcount.values())
        finalv.sort(reverse=True)
        finalv=[finalv[k] for k in range(0,k)]
        finalk=[]
        for x,y in numcount.items():
            if y in finalv:
                finalk.append(x)
        return finalk
            
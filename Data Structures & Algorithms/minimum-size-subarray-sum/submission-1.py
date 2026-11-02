class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        l=0
        sumcurr=0
        for r in range(len(nums)):
            sumcurr+=nums[r]
            if sumcurr>=target:
                mini=min(mini,r-l+1)
                while sumcurr>=target:
                    mini=min(mini,r-l+1)
                    sumcurr-=nums[l]
                    l+=1                    
        if mini==float('inf'):
            return 0           
        return mini


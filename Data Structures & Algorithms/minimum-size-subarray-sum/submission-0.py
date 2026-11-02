class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        l=0
        r=0
        sumcurr=0
        while r<len(nums):
            sumcurr+=nums[r]
            if sumcurr>=target:
                mini=min(mini,r-l+1)
                while sumcurr>=target:
                    mini=min(mini,r-l+1)
                    sumcurr-=nums[l]
                    l+=1
                    
            r+=1
        if mini==float('inf'):
            return 0           
        return mini


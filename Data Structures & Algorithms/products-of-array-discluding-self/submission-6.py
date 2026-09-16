class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        lp=[]
        rp=[]
        final=[]
        for i in range(0,len(nums)):
            if i==0:
                lp.append(1)
            else:
                l*=nums[i-1]
                lp.append(l)
        nums.reverse()
        for j in range(0,len(nums)):
            if j==0:
                rp.append(1)
            else:
                r*=nums[j-1]
                rp.append(r)
        nums.reverse()
        rp.reverse()
        for k in range(0,len(nums)):
            final.append(lp[k]*rp[k])
        return final

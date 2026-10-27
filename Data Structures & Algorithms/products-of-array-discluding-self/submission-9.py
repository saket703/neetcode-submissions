class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod=[1]
        rightprod=[1]
        for i in range(1,len(nums)):
            leftprod.append(leftprod[-1]*nums[i-1])
            rightprod.append(rightprod[-1]*nums[-i])
           
        rightprod.reverse()
        return [x*y for x,y in zip(leftprod,rightprod)]
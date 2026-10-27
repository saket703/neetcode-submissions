class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=len(nums)-2
        leftprod=[1]
        rightprod=[1]
        for i in range(1,len(nums)):
            leftprod.append(leftprod[-1]*nums[left-1])
            rightprod.append(rightprod[-1]*nums[right+1])
            left+=1
            right-=1
        rightprod.reverse()
        return [x*y for x,y in zip(leftprod,rightprod)]
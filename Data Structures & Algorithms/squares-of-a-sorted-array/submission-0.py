class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final=deque()
        r=len(nums)-1
        l=0
        while l<=r:
            if abs(nums[l])>=abs(nums[r]):
                final.appendleft(pow(nums[l],2))
                l+=1
            else:
                final.appendleft(pow(nums[r],2))
                r-=1
        return list(final)

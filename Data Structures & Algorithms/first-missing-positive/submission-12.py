class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        sum1=0
        sum2=0
        if max(nums)>0:
            while min(nums)<1:
                nums.discard(min(nums))
            if min(nums)>1:
                return 1
            

            while True:
                if min(nums)+1 in nums:
                    nums.discard(min(nums))
                else:
                    return min(nums)+1
                
        else:
            return 1

            
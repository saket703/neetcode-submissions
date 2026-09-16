class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        
        maxim =1
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1  
            elif nums[i]==nums[i-1]:
                continue
            else:
                if count>maxim:
                    maxim=count
                count=1
            if count>maxim:
                    maxim=count                        
        return maxim
        
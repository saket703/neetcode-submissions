class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[]
        CompletedTargets=set()
        for i in range(0,len(nums)):
            target=-nums[i]
            LP=i+1
            RP=len(nums)-1
            if nums[i] in CompletedTargets:
                continue
            CompletedTargets.add(nums[i])
            while LP<RP:
                if nums[LP]+nums[RP]<target:
                    LP+=1
                elif nums[LP]+nums[RP]>target:
                    RP-=1
                elif nums[LP]+nums[RP]==target:
                    final.append([nums[LP],nums[RP],nums[i]])
                    currentl=nums[LP]
                    currentr=nums[RP]
                    while currentl==nums[LP] and currentr==nums[RP] and LP<RP:
                        LP+=1
                        RP-=1

        return final
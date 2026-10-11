class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
            else:
                j+=1
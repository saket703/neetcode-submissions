class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LP=0
        RP=len(numbers)-1
        while True:
            if numbers[LP]+numbers[RP]==target:
                return [LP+1,RP+1]
            elif numbers[LP]+numbers[RP]<target:
                LP+=1
            elif numbers[LP]+numbers[RP]>target:
                RP-=1
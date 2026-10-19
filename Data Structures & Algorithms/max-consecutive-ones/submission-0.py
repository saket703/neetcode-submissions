class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        current=0
        for i in nums:
            if i==1:
                current+=1
            else:
                if current>maximum:
                    maximum=current
                current=0
        return max(maximum,current)
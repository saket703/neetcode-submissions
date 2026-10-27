class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        current=0
        curnum=0
        maxim=0
        for i in numset:
            current=0
            if i-1 not in numset:
                curnum=i
                while curnum in numset:
                    current+=1
                    curnum+=1
            maxim=max(current,maxim)

        return maxim
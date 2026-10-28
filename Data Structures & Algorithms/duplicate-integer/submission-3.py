class Solution:
    def hasDuplicate(self, nums):
        counter=defaultdict(int)
        for i in nums:
            counter[i]+=1
            if counter[i]>1:
                return True
        return False
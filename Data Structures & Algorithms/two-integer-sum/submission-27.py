class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsindex=defaultdict(list)
        for index,element in enumerate(nums):            
            numsindex[element].append(index)
        for i in nums:
            if target-i in numsindex and i==target-i:
                if len(numsindex[i])==1:
                    continue
                else:
                    return numsindex[i]
            if target-i in numsindex and i!=target-i:
                return [numsindex[i][0],numsindex[target-i][0]]   
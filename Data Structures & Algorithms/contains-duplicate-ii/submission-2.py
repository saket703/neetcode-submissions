class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        seen=defaultdict(int)
        for r in range(len(nums)):
            seen[nums[r]]+=1
            if seen[nums[r]]==2:
                while seen[nums[l]]!=2:
                    seen[nums[l]]-=1
                    l+=1
                if r-l<=k:
                    return True
                seen[nums[l]]-=1
                l+=1
        return False


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque()
        final=[]
        for i in range(k):
            while queue and nums[i]>=nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for r in range(k-1,len(nums)):
            
            while queue and nums[r]>= nums[queue[-1]]:
                queue.pop()
            queue.append(r)
            while r-queue[0]>=k:
                queue.popleft()
            final.append(nums[queue[0]])

        return final  
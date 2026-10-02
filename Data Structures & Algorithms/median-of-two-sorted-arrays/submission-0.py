class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=nums1+nums2
        x.sort()
        if len(x)%2==1:
            return x[int((len(x)-1)/2)]
        else:
            return (x[int((len(x)-1)/2)]+x[int((len(x)+1)/2)])/2
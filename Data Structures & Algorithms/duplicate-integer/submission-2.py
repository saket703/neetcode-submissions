class Solution:
    def hasDuplicate(self, nums):
        l2 = []

        for j in nums:
            if j not in l2:
                l2.append(j)
            else:
                return True

        return False
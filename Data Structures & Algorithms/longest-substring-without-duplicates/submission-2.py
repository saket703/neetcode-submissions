class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxwindow=0
        left=0
        for right,i in enumerate(s):
            if i in seen:
                while i in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(i)
            maxwindow=max(maxwindow,right-left+1)
        return maxwindow
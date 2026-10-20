class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxim=0
        l=0
        for r,letter in enumerate(s):
            if letter in seen:
                while s[l]!=letter:
                    seen.remove(s[l])
                    l+=1
                seen.remove(s[l])
                l+=1
            seen.add(letter)
            maxim=max(maxim,r-l+1)
        return maxim
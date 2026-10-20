class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxim=0
        l=0
        for letter in s:
            if letter in seen:
                maxim=max(maxim,len(seen))
                while s[l]!=letter:
                    seen.remove(s[l])
                    l+=1
                seen.remove(s[l])
                l+=1
            seen.add(letter)
        return max(maxim,len(seen))
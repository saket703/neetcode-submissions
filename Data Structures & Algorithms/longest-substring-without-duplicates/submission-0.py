class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        elements=set()
        final=0
        maxim=0
        for i in s:
            if i in elements:
                
                while True:
                    if final>maxim:
                        maxim=final
                    a=window.pop(0)
                    elements.remove(a)
                    final-=1
                    if a==i:
                        break
            elements.add(i)
            window.append(i)
            final+=1
            if final>maxim:
                maxim=final
        return maxim


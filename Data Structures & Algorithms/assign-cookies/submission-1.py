class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1=0
        p2=0
        final=0
        for p2 in range(len(s)):
            if p1>=len(g):
                break
            if s[p2]>=g[p1]:
                final+=1
                p1+=1
        return final

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False 
        scount=Counter(s)
        tcount=Counter(t)
        for i in scount:
            if scount[i]!=tcount[i]:
                return False
        return True
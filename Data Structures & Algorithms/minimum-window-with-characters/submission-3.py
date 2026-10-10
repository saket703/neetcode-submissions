class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        l=0
        charscount1=Counter(t)
        window=defaultdict(int)
        res,resLen=[-1,-1],float("infinity")
        have,need=0,len(charscount1)
        for r,elem in enumerate(s):
            window[elem]+=1
            if elem in charscount1 and window[elem]==charscount1[elem]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in charscount1 and window[s[l]]<charscount1[s[l]]:
                    have-=1
                l+=1

        return s[res[0]:res[1]+1] if resLen!=float("infinity") else ""


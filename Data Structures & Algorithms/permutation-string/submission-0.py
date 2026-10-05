class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s11=defaultdict(int)
        s12=defaultdict(int)
        r=len(s1)-1
        for i in s1:
            s11[i]+=1
        for j in s2[0:len(s1)]:
            s12[j]+=1
        for k in range(0,len(s2)-len(s1)+1):
            if s11==s12:
                return True
            elif s11!=s12 and r<len(s2)-1:
                r+=1
                s12[s2[r]]+=1
                if s12[s2[k]]>1:
                    s12[s2[k]]-=1
                else:
                    s12.pop(s2[k])
        return False
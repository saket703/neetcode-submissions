class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for n,item in enumerate(strs):
            s+=str(len(item))
            s+="#"
            s+=item
        return s
        
    def decode(self, s: str) -> List[str]:
        final=[]
        i=0
        j=0
        l=0
        while j<len(s):
            if s[j]=="#":
                l=int(s[i:j])
                final.append(s[j+1:j+1+l])
                i+=(l+2)
                j+=(l+2)
                
            elif s[j]!="#":
                while s[j]!="#":
                    j+=1
                l=int(s[i:j])
                final.append(s[j+1:j+1+l])
                i+=(l+2+(len(str(l))-1))
                j+=(l+2)
        return final

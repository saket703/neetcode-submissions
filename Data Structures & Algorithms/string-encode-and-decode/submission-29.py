class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        k=0
        for i in strs:
            s+=i
            k+=1
            if k<len(strs):
                s+="π"
        if strs!=[]:    
            return s
        elif strs==[]:
            s="ππ"
            return s
    def decode(self, s: str) -> List[str]:
        if s=="ππ":
            return []
        return s.split("π")        
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for string in strs:
            encoded+=str(len(string))+"$"+string
        return encoded

    def decode(self, s: str) -> List[str]:
        l=0
        r=0
        curr=0
        decoded=[]
        while True and s:
            if s[r].isdigit():
                r+=1
            else:
                curr=int(s[l:r])
                decoded.append(s[r+1:r+1+curr])
                if r + 1 + curr < len(s):
                    l, r = r + 1 + curr, r + 1 + curr
                else:
                    break       
        return decoded 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out=[0]*len(temperatures)
        stack=[]
        x=int()
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]] :
                x=stack.pop()
                out[x]=i-x
            stack.append(i)
        return out
class Solution:
    def isValid(self, s: str) -> bool:
        brackets={")":"(","]":"[","}":"{"}
        stack=[]
        
        for i in range(0,len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            elif s[i] in brackets : 
                if len(stack)!=0 and brackets[s[i]]==stack[-1] :
                    stack.pop()
                else:
                    return False
        return stack==[]

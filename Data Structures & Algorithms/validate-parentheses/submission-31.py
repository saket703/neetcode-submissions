class Solution:
    def isValid(self, s: str) -> bool:
        brackets={")":"(","]":"[","}":"{"}
        stack=[]
        
        for i in range(0,len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            elif s[i] in brackets : 
                if stack and stack[-1] == brackets[s[i]]:
                    stack.pop()
                else:
                    return False
        return stack==[]

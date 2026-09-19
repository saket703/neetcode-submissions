class Solution:
    def isPalindrome(self, s: str) -> bool:
        LP=0
        RP=len(s)-1
        while LP<RP:
            if s[LP].isalnum()==False:
                LP+=1
            elif s[RP].isalnum()==False:
                RP-=1
            elif s[LP].lower()==s[RP].lower():
                LP+=1
                RP-=1
                continue
            else:
                return False
        
        return True
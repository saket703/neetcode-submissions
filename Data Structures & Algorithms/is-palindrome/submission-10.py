class Solution:
    def isPalindrome(self, s: str) -> bool:
        LP=0
        RP=len(s)-1
        while LP<RP:
            if s[LP].isalpha()==False and s[LP].isdigit()==False:
                LP+=1
                continue
            if s[RP].isalpha()==False and s[RP].isdigit()==False:
                RP-=1
                continue
            if s[LP].lower()==s[RP].lower():
                LP+=1
                RP-=1
                continue
            else:
                return False
        
        return True
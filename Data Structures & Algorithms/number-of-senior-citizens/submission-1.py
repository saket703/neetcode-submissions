class Solution:
    def countSeniors(self, details: List[str]) -> int:
        final=0
        for i in details:
            if int(i[11:13])>60:
                final+=1
        return final
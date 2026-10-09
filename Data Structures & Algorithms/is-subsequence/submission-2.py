class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        search_string=deque(s)
        for i in t:
            if search_string and i==search_string[0]:
                search_string.popleft()
            if len(search_string)==0:
                return True
        return False

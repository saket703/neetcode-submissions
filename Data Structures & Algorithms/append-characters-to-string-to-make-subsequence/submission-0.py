from collections import Counter
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a=deque(t)
        for i in s:
            if a and i==a[0]:
                a.popleft()
        return len(a)
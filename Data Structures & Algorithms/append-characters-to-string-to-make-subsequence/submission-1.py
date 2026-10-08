class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a=deque(t)
        for i in s:
            if a and i==a[0]:
                a.popleft()
            if not a:
                return 0
        return len(a)
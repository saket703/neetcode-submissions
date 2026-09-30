from math import sqrt
class Solution:
    def climbStairs(self, n: int) -> int:
           
        phi = (1 + sqrt(5)) / 2
        def a(n):
            return round(phi**(n+1) / sqrt(5))
        return a(n) 
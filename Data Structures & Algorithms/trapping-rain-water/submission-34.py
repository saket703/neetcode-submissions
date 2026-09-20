class Solution:
    def trap(self, height: List[int]) -> int:
        mx = max(height)  # computed once, O(n)
        total = len(height) * mx - sum(height)

        maxbarl = 0
        maxbarr = 0
        LP = 0
        RP = len(height) - 1

        while height[LP] != mx or height[RP] != mx:
            if height[LP] != mx:
                maxbarl = max(maxbarl, height[LP])
                total -= mx - maxbarl
                LP += 1
            if height[RP] != mx:
                maxbarr = max(maxbarr, height[RP])
                total -= mx - maxbarr
                RP -= 1

        return total
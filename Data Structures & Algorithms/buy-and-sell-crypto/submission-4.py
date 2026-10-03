class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =prices[0]
        best =0
        for p in prices[1:]:
            if p <buy:
                buy =p              
            else:
                best = max(best, p-buy)   
        return best
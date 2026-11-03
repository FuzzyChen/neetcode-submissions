class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float('inf')
    
        for i in range(len(prices)-1):
            minPrice = (min(minPrice,prices[i]))
            res = max(res,prices[i+1]-minPrice)
        return res
        
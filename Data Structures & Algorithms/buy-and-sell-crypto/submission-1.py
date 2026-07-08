class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        low = prices[0]
        l = 0
        while l < len(prices)-1:
            low = min(low,prices[l])
            l += 1
            res = max(res, prices[l] - low)

        return res
        
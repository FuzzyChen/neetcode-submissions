class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        lowArr = [prices[0]]
        for i in range(1,len(prices)):
            lowArr.append(min(lowArr[i-1],prices[i]))
        for i in range(1,len(prices)):
            res = max(res, prices[i] - lowArr[i])

        return res
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        res= maxPile
        l,r = 1, maxPile
        while l<=r:
            mid = (l+r)//2
            hour = 0
            for p in piles:
                hour += math.ceil(p/mid)
            if hour <= h:
                 r = mid-1
                 res = min(res,mid)
            else:
                l  = mid + 1
        return res
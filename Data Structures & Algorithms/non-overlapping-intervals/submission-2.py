class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1]))
        curEnd = -float('inf')
        res = 0
        for start,end in intervals:
            if start < curEnd:
                res += 1
            else:
                curEnd = end
            
        return res
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count,res = 0,0
        startArr = [meeting.start for meeting in intervals]
        endArr = [meeting.end for meeting in intervals]
        startArr.sort()
        endArr.sort()
        s,e=0,0
        while s< len(startArr):
            if startArr[s]<endArr[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res,count)
        return res
        
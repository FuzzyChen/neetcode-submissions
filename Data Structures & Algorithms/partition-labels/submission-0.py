class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        end = 0
        start = 0
        for index,ch in enumerate(s):
            last[ch] = index
        print(last)
        for i,ch in enumerate(s):
            end = max(end,last[ch])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res
        #merge the intervals
        
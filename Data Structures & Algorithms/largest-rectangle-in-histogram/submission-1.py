class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        l = len(heights)
        for i in range(l):
            min_height = heights[i]
            for j in range(i,l):
                x = j-i+1
                min_height = min(min_height,heights[j])
                res = max(res,x*min_height)
        return res
        
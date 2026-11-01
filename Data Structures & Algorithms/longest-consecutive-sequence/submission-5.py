class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_num = sorted(nums)
        maxL = 1
        res = 1
        for i,num in enumerate(sorted_num):
            if i>0 and sorted_num[i] - sorted_num[i-1] == 0:
                continue
            if i>0 and sorted_num[i] - sorted_num[i-1] == 1:
                maxL+=1
                res = max(res,maxL)
            else:
                maxL = 1
        return res

        
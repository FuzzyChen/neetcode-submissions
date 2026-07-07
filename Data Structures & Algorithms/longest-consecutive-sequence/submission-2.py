class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        res = 0
        for num in nums:
            if num-1 in numSet:
                tmp = 1
                while num+tmp in numSet:
                    tmp += 1
                res = max(res,tmp)
        return res+1
        
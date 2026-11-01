class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums_set = set(nums)

        res = 0
        for num in nums_set:
            if num-1 not in nums_set:
                cur = num
                length = 1
                while num+1 in nums_set:
                    num += 1
                    length+=1
                res = max(res,length)
        return res

        
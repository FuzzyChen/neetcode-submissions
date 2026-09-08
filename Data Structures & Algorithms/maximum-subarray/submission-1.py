class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preMax = nums[0]
        res = preMax
        # [2,-1,4,......] 
        for i in range(1,len(nums)):
            if preMax<0:
                preMax = nums[i]
            else:
                preMax = nums[i] + preMax
            res = max(res,preMax)
        return res
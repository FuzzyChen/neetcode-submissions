class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        resArr = [-float("inf") ]* len(nums)
        
        # [2,-1,4,......] 
        for i in range(len(nums)):
            if i==0:
                resArr[0] = nums[0]
            else:
                if resArr[i-1]<0:
                    resArr[i] = nums[i]
                else:
                    # print(i)
                    resArr[i] = nums[i] + resArr[i-1]

        return max(resArr)
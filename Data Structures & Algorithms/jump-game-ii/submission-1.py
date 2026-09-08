class Solution:
    def jump(self, nums: List[int]) -> int:
        resArr = [float("inf")] * len(nums)
        resArr[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            # print(i)
            if i+nums[i]>=len(nums)-1:
                resArr[i] = 1
            else:
                resArr[i] = 1+ min(resArr[i: i+nums[i]+1])
        # print(resArr)
        return resArr[0]
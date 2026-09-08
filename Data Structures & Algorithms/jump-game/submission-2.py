class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return True
        
        nums[-1] = True
        n = len(nums)
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= n or nums[i+nums[i]] is True:
                end = min(n,i+i+nums[i]+1)
                for l in range(i,end):
                    nums[l] = True
            else:
                nums[i] = False
        print(nums)
        return nums[0]
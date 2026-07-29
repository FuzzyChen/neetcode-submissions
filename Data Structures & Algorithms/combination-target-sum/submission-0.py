class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not target:
            return []
        self.res = []
        self.backtrack(nums,0,[],target)
        return self.res



    def backtrack(self,nums,start,track,target):
        if(sum(track) == target):
            self.res.append(track.copy())
            return
        if(sum(track) > target):
            return
        for i in range(start,len(nums)):
            track.append(nums[i])
            self.backtrack(nums,i,track,target)
            track.pop()

            
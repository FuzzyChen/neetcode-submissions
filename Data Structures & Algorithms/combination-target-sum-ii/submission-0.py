class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not target:
            return []
        self.res = []
        candidates.sort()
        self.backtrack(candidates,0,[],target)
        return self.res



    def backtrack(self,nums,start,track,target):
        if(sum(track) == target):
            self.res.append(track.copy())
            return
        if(sum(track) > target):
            return
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            track.append(nums[i])
            self.backtrack(nums,i+1,track,target)
            track.pop()
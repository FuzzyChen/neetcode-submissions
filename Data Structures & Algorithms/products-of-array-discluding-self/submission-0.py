class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            restTotal = 1
            for index,num in enumerate(nums):
                if index!=i:
                    restTotal *= num
            res.append(restTotal)
        return res
        
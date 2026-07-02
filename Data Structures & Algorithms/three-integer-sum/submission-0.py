class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for startIndex in range(len(nums) - 2):
            # Skip duplicate start values
            if startIndex > 0 and nums[startIndex] == nums[startIndex - 1]:
                continue
            
            left = startIndex + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[startIndex] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[startIndex], nums[left], nums[right]])
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res




        
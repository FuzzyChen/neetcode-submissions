class Solution:
    def findMin(self, nums: List[int]) -> int:
        # differnt conditions with binary search

        l,r = 0,len(nums)-1
        
        while  l < r:
            mid = (l+r)//2
            # compare mid with r, if mid > r then the minimal is in right 
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]
            

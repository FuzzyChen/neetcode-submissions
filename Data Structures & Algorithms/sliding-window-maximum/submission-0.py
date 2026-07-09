class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        
        window = deque(nums[:k])
        res = []
        for r in range(k,len(nums)):
            res.append(max(window))
            window.popleft()
            window.append(nums[r])
        res.append(max(window))
        return res
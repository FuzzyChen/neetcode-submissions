class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        for ch in s:
            while ch in window:
                window.remove(s[l])
                l += 1
            window.add(ch)
            res = max(res,len(window))
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        res = 0

        for ch in s:
            while ch in window:
                window.remove(s[l])
                l += 1

            window.add(ch)
            res = max(res, len(window))

        return res
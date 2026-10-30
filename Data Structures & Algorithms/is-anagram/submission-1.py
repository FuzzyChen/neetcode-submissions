class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        for ch in t:
            if ch in dic:
                dic[ch] -= 1
            else:
                return False
        for k in dic:
            if dic[k] != 0:
                return False
        return True

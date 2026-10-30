class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        a = [0]*26
        for ch in s:
            a[ord(ch)-ord('a')] += 1

        for ch in t:
            i = ord(ch)-ord('a')
            a[i] -= 1
            if a[i] < 0:
                return False

        return sum(a) == 0

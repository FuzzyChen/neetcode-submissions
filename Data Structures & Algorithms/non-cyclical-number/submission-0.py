class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        cur = n
        while cur not in s:
            
            if cur == 1:
                return True
            s.add(cur)
            nextNum = 0
            while cur >= 10:
                nextNum += (cur % 10) ** 2
                cur = cur // 10
            cur = nextNum + (cur % 10) ** 2
        return False

class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight( n: int) -> int:
            res = 0
            while n > 1:
                res += n % 2
                n = n // 2
            return res + n
        resArr = []
        for i in range(n+1):
            resArr.append(hammingWeight(i))
        return resArr
        
class Solution:
    def reverseBits(self, n: int) -> int:
        bit = ''
        for i in range(32):
            d = n % 2
            n = n // 2
            bit += str(d)
        start = 1
        res = 0
        for i in range(32):
            res +=  2 ** i * int(bit[31-i])
        return res

        
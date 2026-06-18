class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = 1 & (n >> (31 - i))
            res |= bit << i
        return res
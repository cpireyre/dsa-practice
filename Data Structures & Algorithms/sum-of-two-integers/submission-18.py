class Solution:
    def getSum(self, a: int, b: int) -> int:
        intmax = 0x7fffffff
        mask   = 0xffffffff
        while b:
            carry = (a&b)<<1
            a = (a^b)&mask
            b = carry
        return a if a <= intmax else ~(a^mask)
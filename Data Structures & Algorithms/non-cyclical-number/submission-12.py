def succ(n):
    res = 0
    while n:
        d = n % 10
        res += d**2
        n //= 10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        a,b = n,n
        while True:
            a,b = succ(a),succ(succ(b))
            if a == 1 or b == 1: return True
            if a == b: return False
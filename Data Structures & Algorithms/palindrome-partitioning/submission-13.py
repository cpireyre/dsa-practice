def pal(xs):
    l,r = 0,len(xs)-1
    while l < r:
        if xs[l] != xs[r]: return False
        l += 1; r -= 1
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def f(xs, l):
            if l == len(s):
                res.append(xs[:])
                return
            for r in range(l, len(s)):
                if not pal(s[l:r+1]): continue
                xs.append(s[l:r+1])
                f(xs, r+1)
                xs.pop()
        f([],0)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,res,maxf = 0,0,0
        D = defaultdict(int)
        for r,c in enumerate(s):
            D[c] += 1
            maxf = max(maxf, D[c])
            while r - l + 1 - maxf > k:
                D[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
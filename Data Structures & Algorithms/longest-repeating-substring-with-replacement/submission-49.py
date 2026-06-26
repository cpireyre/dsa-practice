class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = maxf = 0
        C = defaultdict(int)
        for r,c in enumerate(s):
            C[c] += 1
            maxf = max(maxf, C[c])
            if r - l + 1 - maxf > k:
                C[s[l]] -= 1; l += 1
            res = max(res, r - l + 1)
        return res
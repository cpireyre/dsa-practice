class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0
        count = defaultdict(int)
        for r,c in enumerate(s):
            count[c] += 1
            maxf = max(maxf, count[c])
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        C = defaultdict(int)
        l = 0
        res = 0
        for r,c in enumerate(s):
            C[c] += 1
            while C[c] > 1:
                C[s[l]] -= 1; l += 1
            res = max(res, r - l + 1)
        return res
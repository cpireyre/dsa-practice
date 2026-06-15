class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res,xs = 0,0,set()
        for r,c in enumerate(s):
            while c in xs:
                xs.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            xs.add(c)
        return res
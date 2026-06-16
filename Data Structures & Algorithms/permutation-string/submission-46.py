class Solution:
# True if P(s1) ⊂ s2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        win,count = [0]*26,[0]*26
        al = lambda c: ord(c) - ord('a')
        for i in range(len(s1)):
            count[al(s1[i])] += 1
            win[al(s2[i])] += 1
        matches = sum(w==c for w,c in zip(win,count))
        match = lambda c: win[c] == count[c]
        l = 0
        for r,c in enumerate(s2[len(s1):]):
            if matches == 26: return True
            p,q = al(c),al(s2[l])
            matches -= match(p) + match(q)
            win[p] += 1; win[q] -= 1; l += 1
            matches += match(p) + match(q)
        return matches == 26
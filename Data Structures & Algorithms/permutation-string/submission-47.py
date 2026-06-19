class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        win, count = [0] * 26, [0] * 26
        al = lambda c: ord(c) - ord('a')
        for i in range(len(s1)):
            count[al(s1[i])] += 1
            win[al(s2[i])] += 1
        match = lambda c: count[c] == win[c]
        matches = sum(match(i) for i in range(26))
        l = 0
        for r,c in enumerate(s2[len(s1):]):
            if matches == 26: return True
            p,q = al(c),al(s2[l])
            matches -= match(p) + match(q)
            win[p] += 1; win[q] -= 1; l += 1
            matches += match(p) + match(q)
        return matches == 26
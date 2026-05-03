class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        al = lambda c: ord('a') - ord(c)
        for s in strs:
            h = [0] * 26
            for c in s: h[al(c)] += 1
            res[tuple(h)].append(s)
        return list(res.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        al = lambda c: ord(c) - ord('a')
        res = defaultdict(list)
        for s in strs:
            xs = [0]*26
            for c in s: xs[al(c)] += 1
            res[tuple(xs)].append(s)
        return list(res.values())
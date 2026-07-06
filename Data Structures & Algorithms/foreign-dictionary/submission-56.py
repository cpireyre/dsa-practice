class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        D,G = {c:0 for c in chain(*words)},defaultdict(set)
        for w,q in pairwise(words):
            if len(w) > len(q) and w[:len(q)] == q: return ""
            mismatch = next((p for p in zip(w,q) if p[0]!=p[1]),None)
            if mismatch:
                u,v = mismatch
                D[v] += v not in G[u]; G[u].add(v)
        Q,S = deque(v for v in D if not D[v]),list()
        while Q:
            u = Q.popleft(); S.append(u)
            for v in G[u]:
                D[v] -= 1
                if not D[v]: Q.append(v)
        return "".join(S) if len(S) == len(D) else ""
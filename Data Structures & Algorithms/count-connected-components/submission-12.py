class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [0] * (n + 1)
    def find(self,u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def unite(self,u,v):
        u,v = self.find(u),self.find(v)
        if u == v: return False
        if self.size[u] < self.size[v]: u,v = v,u
        self.parent[v] = u
        self.size[u] += self.size[v]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = DSU(n)
        return n - sum(G.unite(*e) for e in edges)
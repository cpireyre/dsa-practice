class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [0]*(n+1)
    def find(self,u):
        if u != self.parent[u]:
            u = self.find(self.parent[u])
        return self.parent[u]
    def unite(self,u,v):
        u,v = self.find(u),self.find(v)
        if u == v: return False
        if self.size[u] < self.size[v]: u,v = v,u
        self.size[u] += self.size[v]
        self.parent[v] = u
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        inside = lambda r,c: 0<=r<R and 0<=c<C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        land = lambda r,c: grid[r][c] == "1"
        idx = lambda r,c: r*C + c
        res = 0
        G = DSU(R*C)
        for u in product(range(R),range(C)):
            if not land(*u): continue
            res += 1
            for v in neighbors(*u):
                if not inside(*v): continue
                if not land(*v): continue
                res -= G.unite(idx(*u), idx(*v))
        return res
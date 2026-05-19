class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights),len(heights[0])
        inside = lambda r,c: 0<=r<R and 0<=c<C
        neighbors = lambda r,c: [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        h = lambda r,c: heights[r][c]
        def bfs(Q):
            Q = deque(Q)
            S = set()
            while Q:
                u = Q.popleft(); S.add(u)
                for v in neighbors(*u):
                    if v in S: continue
                    if not inside(*v): continue
                    if h(*v) >= h(*u): Q.append(v)
            return S
        top = [(0,c) for c in range(C)]
        bottom = [(R-1,c) for c in range(C)]
        left = [(r,0) for r in range(R)]
        right = [(r,C-1) for r in range(R)]
        return list(bfs(top + left) & bfs(bottom + right))

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D,G = defaultdict(int),defaultdict(set)
        for u,v in prerequisites:
            D[v] += 1; G[u].add(v)
        Q,S = deque(v for v in range(numCourses) if not D[v]), list()
        while Q:
            u = Q.popleft(); S.append(u)
            for v in G[u]:
                D[v] -= 1
                if not D[v]: Q.append(v)
        return len(S) == numCourses
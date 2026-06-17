class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x,y: x**2 + y**2
        xs = []
        for p in points:
            heapq.heappush(xs, (dist(*p), p))
        return [p for _,p in heapq.nsmallest(k,xs)]
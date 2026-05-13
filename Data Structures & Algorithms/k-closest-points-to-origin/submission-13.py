class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        xs = []
        for x,y in points:
            heapq.heappush(xs, (-(x**2+y**2),x,y))
            if len(xs) > k: heapq.heappop(xs)
        return [(x,y) for _,x,y in xs]
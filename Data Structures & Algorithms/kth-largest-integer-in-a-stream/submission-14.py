class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.xs = []
        for n in nums: heapq.heappush(self.xs, n)
        while len(self.xs) > self.k: heapq.heappop(self.xs)
    def add(self, val: int) -> int:
        heapq.heappush(self.xs, val)
        if len(self.xs) > self.k: heapq.heappop(self.xs)
        return self.xs[0]

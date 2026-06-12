class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.xs = nums[:]
        self.k = k
        heapq.heapify(self.xs)
        while len(self.xs) > self.k: heapq.heappop(self.xs)

    def add(self, val: int) -> int:
        heapq.heappush(self.xs, val)
        if len(self.xs) > self.k: heapq.heappop(self.xs)
        return self.xs[0]
class MedianFinder:
    def __init__(self):
        self.bigs = []
        self.smol = []

    def addNum(self, num: int) -> None:
        if self.bigs and self.bigs[0] <= num:
            heapq.heappush(self.bigs, num)
        else: heapq.heappush(self.smol, -num)
        if len(self.bigs) > len(self.smol):
            n = -heapq.heappop(self.bigs)
            heapq.heappush(self.smol,n)
        if len(self.smol) > len(self.bigs):
            n = -heapq.heappop(self.smol)
            heapq.heappush(self.bigs, n)

    def findMedian(self) -> float:
        if len(self.bigs) > len(self.smol): return self.bigs[0]
        if len(self.smol) > len(self.bigs): return -self.smol[0]
        return (self.bigs[0] - self.smol[0]) / 2
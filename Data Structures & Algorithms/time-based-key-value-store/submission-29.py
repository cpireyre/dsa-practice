class TimeMap:
    def __init__(self):
        self.xs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.xs[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        ys = self.xs[key]
        l,r = 0,len(ys)-1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            t,v = ys[m]
            if t <= timestamp:
                res = v
                l = m + 1
            else: r = m -1
        return res
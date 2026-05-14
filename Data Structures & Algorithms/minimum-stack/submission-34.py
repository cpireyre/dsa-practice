class MinStack:
    def __init__(self):
        self.xs = []
        self.mins = []

    def push(self, val: int) -> None:
        self.xs.append(val)
        v = val if not self.mins or val < self.mins[-1] else self.mins[-1]
        self.mins.append(v)

    def pop(self) -> None:
        self.xs.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.xs[-1]

    def getMin(self) -> int:
        return self.mins[-1]
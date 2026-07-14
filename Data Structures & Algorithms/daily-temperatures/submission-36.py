class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res,xs = [0]*len(temperatures),[]
        for i,t in enumerate(temperatures):
            while xs and temperatures[xs[-1]] < t:
                j = xs.pop()
                res[j] = i - j
            xs.append(i)
        return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s,e in intervals[1:]:
            if res[-1][1] < s: res.append([s,e])
            else: res[-1][1] = max(e,res[-1][1])
        return res
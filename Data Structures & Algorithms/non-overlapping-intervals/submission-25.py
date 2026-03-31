class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        res = 0
        prevEnd = intervals[0][1]
        for s,e in intervals[1:]:
            if s < prevEnd: res += 1
            else: prevEnd = e
        return res
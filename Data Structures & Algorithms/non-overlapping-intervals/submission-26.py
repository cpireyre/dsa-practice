class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        prevEnd = intervals[0][1]
        res =0
        for s,e in intervals[1:]:
            if prevEnd > s: res += 1
            else: prevEnd = max(prevEnd, e)
        return res
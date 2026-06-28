class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda i:i[1])
        prevEnd = intervals[0][1]
        for s,e in intervals[1:]:
            if prevEnd > s: res += 1
            else: prevEnd=  e
        return res
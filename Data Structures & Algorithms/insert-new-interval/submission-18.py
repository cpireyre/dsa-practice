class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,(s,e) in enumerate(intervals):
            if   newInterval[1] < s: return res + [newInterval] + intervals[i:]
            elif newInterval[0] > e: res.append([s,e])
            else: newInterval = [min(s,newInterval[0]),max(e,newInterval[1])]
        res.append(newInterval)
        return res
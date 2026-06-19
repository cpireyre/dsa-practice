"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        M = defaultdict(int)
        for i in intervals: M[i.start] += 1; M[i.end] -= 1
        res = current = 0
        for i in sorted(M.keys()): current += M[i]; res = max(res, current)
        return res
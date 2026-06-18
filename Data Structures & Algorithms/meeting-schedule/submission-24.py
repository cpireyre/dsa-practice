"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        schedule = sorted((i.start,i.end) for i in intervals)
        return all(e <= s for (_,e),(s,_) in pairwise(schedule))
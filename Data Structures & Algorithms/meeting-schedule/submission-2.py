"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if prevEnd > currStart then False
        # Sort intervals by start time
        intervals = sorted(intervals, key=lambda x: x.start)
        if not intervals:
            return True
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i].start:
                return False
            prevEnd = intervals[i].end
        return True
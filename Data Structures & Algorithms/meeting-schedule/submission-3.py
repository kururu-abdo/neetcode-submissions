"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # An empty schedule has zero conflicts
        if not intervals:
            return True
        
        # Sort by start time
        intervals.sort(key=lambda i: i.start)
        
        # Check adjacent intervals for overlap
        for i in range(1, len(intervals)):
            # If the current meeting starts BEFORE the previous meeting ends
            if intervals[i].start < intervals[i - 1].end:
                return False  # Found a conflict, immediately exit
                
        return True  # Looped through all without conflicts

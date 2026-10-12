"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Brute Force Way, (0,30) and (5,10); 2 meetings overlap if the earlier ending time is greater than the later starting time
        for i in range(0, len(intervals)):
            A = intervals[i] # Define Meeting_A
            for j in range(i+1, len(intervals)):
                B = intervals[j] # Define Meeting_B
                # How to define overlap? One short meeting is over, howerver the other meeting start even earlier than that
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True

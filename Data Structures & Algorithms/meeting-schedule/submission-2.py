"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sorting, sorted by starting time of the meeting, and then check one by one if the current starting time of the meeting is smaller than the previous ending time of the meeting
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            CurrentMeeting = intervals[i]
            PreviousMeeting = intervals[i-1]

            if CurrentMeeting.start < PreviousMeeting.end:
                return False
        return True

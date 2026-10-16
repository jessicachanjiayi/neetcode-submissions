"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        i,j = 0,0
        rooms = 0
        max_rooms = 0

        while i < len(intervals):
            if starts[i]< ends[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            max_rooms = max(max_rooms,rooms)
        return max_rooms

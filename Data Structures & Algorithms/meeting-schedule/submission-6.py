"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for meeting in intervals :
            events.append([meeting.start, 1])
            events.append([meeting.end, - 1])

        events.sort(key = lambda x : x[0])
        tmp = 0
        for event, time in events :
            if tmp >= 2 :
                return False
            tmp += time

        return True

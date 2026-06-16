"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count, res = 0, 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        start_idx, end_idx = 0, 0

        while start_idx < len(intervals) :
            if start[start_idx] < end[end_idx] :
                count += 1
                start_idx += 1
            else :
                count -= 1
                end_idx += 1

            res = max(res, count)

        return res
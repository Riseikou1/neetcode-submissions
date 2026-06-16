class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        out = intervals[0][1]
        count = 0

        for interval in intervals[1:] :
            if interval[0] < out :
                count += 1
                out = min(out, interval[1])

            else :
                out = interval[1]

        return count

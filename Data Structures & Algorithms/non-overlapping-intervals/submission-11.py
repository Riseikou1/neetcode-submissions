class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        res = 0

        for start, end in intervals[1:] :
            if start >= prev :
                prev = end
            else : 
                res += 1
                prev = min(prev, end)

        return res

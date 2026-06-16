class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair : pair[0])
        res = []
        prev = intervals[0]
        for start, end in intervals[1:] :
            if start > prev[1] :
                res.append(prev)
                prev = [start, end]
            else :
                prev = [min(start, prev[0]), max(end, prev[1])]

        res.append(prev)
        return res

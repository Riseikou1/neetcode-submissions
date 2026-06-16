class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair : pair[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)) :
            start, end = intervals[i]
            if res[-1][1] >= start :
                res[-1][1] = max(res[-1][1], end)
            else :
                res.append([start, end])

        return res

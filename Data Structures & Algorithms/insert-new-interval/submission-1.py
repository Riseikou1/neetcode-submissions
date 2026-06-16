class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for idx, (start, end) in enumerate(intervals) :
            if end < newInterval[0] :
                res.append([start, end])
            elif newInterval[1] < start :
                res.append(newInterval)
                return res + intervals[idx :]
            else :
                newInterval = [min(start, newInterval[0]), 
                               max(end, newInterval[1])]
        res.append(newInterval)
        return res

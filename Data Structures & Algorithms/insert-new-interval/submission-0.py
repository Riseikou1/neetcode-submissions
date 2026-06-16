class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        target = newInterval[0]
        l, r = 0, len(intervals)

        while l < r :
            m = l + (r - l) // 2
            if intervals[m][0] < target :
                l = m + 1
            else :
                r = m

        intervals.insert(l, newInterval)
        
        res = [intervals[0]]
        for interval in intervals[1:] :
            if res[-1][1] < interval[0] :
                res.append(interval)
            else :
                res[-1][1] = max(interval[1], res[-1][1])

        return res
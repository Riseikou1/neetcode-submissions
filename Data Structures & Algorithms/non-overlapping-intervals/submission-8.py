class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        dp = [1] * len(intervals)
        intervals.sort(key = lambda pair : pair[1])

        for i in range(len(intervals) - 2, -1, -1) :
            for j in range(i + 1, len(intervals)) :
                if intervals[i][1] <= intervals[j][0] :
                    dp[i] = max(dp[i], 1 + dp[j])

        return len(intervals) - max(dp)

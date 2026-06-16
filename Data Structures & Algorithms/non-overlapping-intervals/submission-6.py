class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair : pair[1])
        n = len(intervals)
        dp = [0] * n
        dp[0] = 1

        def bs(target) :
            l, r = 0, n
            while l < r :
                m = (l + r) >> 1
                if intervals[m][1] <= target :
                    l = m + 1
                else :
                    r = m

            return l

        for i in range(1, n) :
            idx = bs(intervals[i][0])
            if idx :
                dp[i] = max(dp[i - 1], 1 + dp[idx - 1])
            else :
                dp[i] = dp[i - 1]

        return n - dp[n - 1]

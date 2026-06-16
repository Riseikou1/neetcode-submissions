class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair : pair[1])
        memo = {}
        n = len(intervals)
        
        def dfs(i) :
            if i in memo : return memo[i]
            res = 1

            for j in range(i + 1, n) :
                if intervals[i][1] <= intervals[j][0] :
                    res = max(res, 1 + dfs(j))

            memo[i] = res
            return res

        return n - dfs(0)

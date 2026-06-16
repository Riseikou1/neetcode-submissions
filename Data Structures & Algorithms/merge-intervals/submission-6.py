class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0] * (max_val + 1)
        for start, end in intervals :
            mp[start] = max(mp[start], end + 1)
            # end + 1 cuz, [1, 2] and [2, 4] intervals are considered as overlapping. at the point 2.
            # so for capturing this behaviour adding additional 1 to end.
        interval_start = -1
        have = -1
        res = []

        for i in range(len(mp)) :
            if mp[i] :
                if interval_start == -1 :
                    interval_start = i
                have = max(have, mp[i] - 1)
            if have == i :
                res.append([interval_start, have])
                have = -1
                interval_start = -1
        if interval_start != -1 :
            res.append([interval_start, have])

        return res
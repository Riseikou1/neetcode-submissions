class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals :
            mp[start] += 1
            mp[end] -= 1

        res, interval = [], []
        have = 0

        for num in sorted(mp) :
            have += mp[num]
            if not interval :
                interval.append(num)

            if have == 0 :
                interval.append(num)
                res.append(interval)
                interval = []

        return res
            
        
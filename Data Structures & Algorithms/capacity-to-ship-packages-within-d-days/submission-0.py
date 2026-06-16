class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def helper(cap) :
            res = 1
            total = 0
            for w in weights :
                if total + w > cap :
                    res += 1
                    total = 0
                    if res > days : return False
                total += w
            return res <= days

        while l < r :
            m = (r + l) // 2
            if helper(m) :
                r = m
            else :
                l = m + 1
        return l
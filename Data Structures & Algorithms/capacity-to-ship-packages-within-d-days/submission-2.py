class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def condition(cap) :
            total, res = 0, 1
            for weight in weights :
                total += weight
                if total > cap :
                    total = weight
                    res += 1

            return res > days

        while l < r :
            mid = (r - l) // 2 + l

            if condition(mid) :
                l = mid + 1

            else :  
                r = mid

        return l
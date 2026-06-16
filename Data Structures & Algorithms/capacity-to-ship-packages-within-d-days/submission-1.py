class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def helper(cap) :
            total = 0
            d = 1

            for num in weights :
                if total + num > cap :
                    total = num
                    d += 1
                else :
                    total += num

            return d <= days

        while l < r :
            mid = (r + l) // 2
            if helper(mid) :
                r = mid
            else :
                l = mid + 1

        return l


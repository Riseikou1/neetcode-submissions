from copy import deepcopy

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = l + (r - l) // 2
            time = 0

            for pile in piles :
                time += math.ceil(pile/k)

            if time <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1

        return min_k

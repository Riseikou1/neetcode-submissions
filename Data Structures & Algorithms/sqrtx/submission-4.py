class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r :
            m = l + (r - l) // 2
            square = m ** 2
            if square == x : 
                return m
            elif square > x :
                r = m - 1
            else :
                l = m + 1
                res = m

        return res


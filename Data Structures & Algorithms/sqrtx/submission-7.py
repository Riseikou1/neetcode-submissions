class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r :
            m = (r + l + 1) // 2

            if m * m > x :
                r = m  - 1
            else :
                l = m

        return l

# since we returning maximum possible kinda shit, 
# we're doing (r + l + 1) shit and l = m
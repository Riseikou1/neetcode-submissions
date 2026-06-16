class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        res = 0

        while x :
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = res * 10 + digit

        return 0 if res < MIN or res > MAX else res

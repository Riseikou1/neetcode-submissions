class Solution:
    def climbStairs(self, n: int) -> int:
        two, one = 1, 1
        if n <= 2 : return n

        for i in range(2, n + 1) :
            tmp = one
            one += two
            two = tmp

        return one
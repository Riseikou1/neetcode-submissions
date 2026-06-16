class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one = 1  # one_step before
        two = 1  # two_steps before

        for _ in range(2, n):
            two, one = one, one + two

        return one + two

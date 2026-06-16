class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum >> 1
        dp = 1
        for stone in stones :
            dp |= dp << stone

        for t in range(target, -1, -1) :
            if dp & (1 << t) :
                return stoneSum - 2 * t

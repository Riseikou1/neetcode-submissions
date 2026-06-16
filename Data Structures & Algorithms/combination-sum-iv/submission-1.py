class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for trg in range(1, target + 1) :
            for num in nums :
                dp[trg] += dp.get(trg - num, 0)

        return dp[target]


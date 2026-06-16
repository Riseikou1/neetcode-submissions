class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 : return False
        target = total >> 1
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums :
            if dp[target] : return True
            for t in range(target, num - 1, -1) :
                dp[t] |= dp[t - num]

        return dp[target]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = nums[n - 1]

        for i in range(n - 2, -1, -1) :
            dp[i] = max(nums[i], dp[i + 1] + nums[i])

        return max(dp)

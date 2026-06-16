class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]

        def helper(lst) :
            if not lst : return 0
            if len(lst) == 1 : return lst[0]

            dp = [0] * len(lst)
            dp[0] = lst[0]
            dp[1] = max(lst[0], lst[1])

            for i in range(2, len(lst)) :
                dp[i] = max(dp[i - 1], lst[i] + dp[i - 2])

            return dp[-1]
        
        return max(helper(nums[1 : ]), helper(nums[: -1]))


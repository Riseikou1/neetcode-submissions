class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]

        memo = {}

        def dfs(i, taken_first) :
            if i >= len(nums) or (taken_first and i == len(nums) - 1) :
                return 0

            if (i, taken_first) in memo :
                return memo[(i, taken_first)]

            memo[(i, taken_first)] = max(dfs(i + 1, taken_first), dfs(i + 2,taken_first) + nums[i])
            return memo[(i, taken_first)]

        return max(dfs(0, True), dfs(1, False))

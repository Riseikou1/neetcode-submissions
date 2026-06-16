class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {len(nums) - 1 : 0}

        def dfs(idx) :
            if idx in memo : 
                return memo[idx]

            end = min(len(nums) - 1, idx + nums[idx])

            res = float('inf')
            for i in range(idx + 1, end + 1) :
                res = min(res, 1 + dfs(i))

            memo[(idx)] = res
            return res

        return dfs(0)

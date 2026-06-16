class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        memo = {(n, 0) : 0}

        def dfs(i, m) :
            if (i, m) in memo : return memo[(i, m)]

            if m == 0 : return float('inf')

            res = float('inf')
            total = 0
            for j in range(i, n - m + 1) :
                total += nums[j]
                res = min(res, max(total, dfs(j + 1, m - 1)))

            memo[(i, m)] = res
            return res

        return dfs(0, k)
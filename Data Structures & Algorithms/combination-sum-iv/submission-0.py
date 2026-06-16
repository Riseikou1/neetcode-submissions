class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {target : 1}

        def dfs(total) :
            if total in memo : return memo[total]

            res = 0
            for num in nums :
                if total + num <= target :
                    res += dfs(total + num)

            memo[total] = res
            return res
        
        return dfs(0)


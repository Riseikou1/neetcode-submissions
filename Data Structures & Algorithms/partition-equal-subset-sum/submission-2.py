class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 : return False
        memo = {(i, 0) : True for i in range(len(nums))}

        def dfs(i, total) :
            if (i, total) in memo : return memo[(i, total)]

            if i >= len(nums) or total < 0 : 
                return False

            res = (dfs(i + 1, total) or dfs(i + 1, total - nums[i]))
            memo[(i, total)] = res
            return res

        return dfs(0, sum(nums) // 2)


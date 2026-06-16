class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(idx, total) :
            if idx == len(nums) :
                return total

            return dfs(idx + 1, total) + dfs(idx + 1, total ^ nums[idx])

        return dfs(0, 0)

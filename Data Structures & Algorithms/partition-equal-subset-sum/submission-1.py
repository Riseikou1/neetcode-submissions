class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 : return False

        def dfs(i, total) :
            if i >= len(nums) :
                return total == 0
            if total < 0 : return False
            
            return (dfs(i + 1, total) or dfs(i + 1, total - nums[i]))

        return dfs(0, summ // 2)


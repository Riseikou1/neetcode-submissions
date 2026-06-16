class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 : return False

        def dfs(idx, cur) :
            if cur == total >> 1 :
                return True

            if cur > total >> 1 :
                return False

            for i in range(idx, len(nums)) :
                if dfs(i + 1, cur + nums[i]) :
                    return True

            return False
        return dfs(0, 0)

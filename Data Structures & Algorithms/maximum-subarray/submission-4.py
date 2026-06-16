class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # implement kanade's algo.
        cur_max, glob_max = float('-inf'), float('-inf')

        for num in nums :
            cur_max = max(num, num + cur_max)
            glob_max = max(glob_max, cur_max)

        return glob_max

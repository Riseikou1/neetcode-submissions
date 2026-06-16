class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # we could use kadane's algo.
        # we iterate through nums array once.
        # while doing that, 
        # we calculate the max and min sub and total sum.
        # and decide whether to take 
        # max subarray or total - min_sub;
        glob_max = float('-inf')
        glob_min = float('inf')
        cur_min, cur_max = 0, 0
        total = 0

        for num in nums :
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)

            glob_max = max(glob_max, cur_max)
            glob_min = min(glob_min, cur_min)

            total += num

        return glob_max if glob_max < 0 else max(glob_max, total - glob_min)

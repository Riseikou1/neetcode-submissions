class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[n - 1] = nums[n - 1]
        cur_sum = nums[n - 1]
        
        for i in range(n - 2, -1, -1) :
            cur_sum += nums[i]
            right_max[i] = max(cur_sum, right_max[i + 1])

        res = nums[0]
        prefix_sum = 0
        cur_max = float("-inf")
        for i in range(n) :
            prefix_sum += nums[i]
            cur_max = max(cur_max + nums[i], nums[i])
            res = max(res, prefix_sum, nums[i], cur_max)

            if i + 1 < n :
                res = max(res, prefix_sum + right_max[i + 1])

        return res

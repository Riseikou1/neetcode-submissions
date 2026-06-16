class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_left = [1] * len(nums)
        cum_right = [1] * len(nums)

        for i in range(1, len(nums)) :
            cum_left[i] = cum_left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1) :
            cum_right[i] = cum_right[i + 1] * nums[i + 1]

        res = []
        for i in range(len(nums)) :
            res.append(cum_left[i] * cum_right[i])

        return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_subarray = [1] * len(nums)
        right_subarray = [1] * len(nums)

        for i in range(1, len(nums)) :
            left_subarray[i] = left_subarray[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1) :
            right_subarray[i] = right_subarray[i + 1] * nums[i + 1]

        return [left_subarray[i] * right_subarray[i] for i in range(len(nums))]

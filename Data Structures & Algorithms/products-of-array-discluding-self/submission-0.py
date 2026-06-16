class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        cur = 1
        for i in range(len(nums)):
            output[i] *= cur
            cur *= nums[i]

        cur = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= cur
            cur *= nums[i]

        return output
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]*len(nums)

        cur = 1
        for i in range(len(nums)):
            result[i] *= cur
            cur *= nums[i]

        cur = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= cur
            cur *= nums[i]

        return result


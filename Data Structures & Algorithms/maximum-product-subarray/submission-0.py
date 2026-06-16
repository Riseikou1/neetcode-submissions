class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums :
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmp * num, num)
            res = max(res, curMax)

        return res
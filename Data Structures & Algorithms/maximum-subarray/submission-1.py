class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, maxi = 0, nums[0]

        for num in nums :
            cur = max(cur + num, num)
            maxi = max(maxi, cur)

        return maxi


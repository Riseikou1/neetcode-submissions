import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        res = 0
        for i in range(len(nums)) :
            if not dp or dp[-1] < nums[i] :
                dp.append(nums[i])
                res += 1
            else :
                l, r = 0, res
                while l < r :
                    m = (r + l) // 2
                    if dp[m] < nums[i] :
                        l = m + 1
                    else :
                        r = m
                dp[l] = nums[i]

        return res

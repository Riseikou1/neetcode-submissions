class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)) :
            if nums[i] > dp[-1] :
                dp.append(nums[i])
                continue

            l, r = 0, len(dp)

            while l < r :
                m = (r + l) // 2
                if dp[m] < nums[i] :
                    l = m + 1
                else :
                    r = m

            dp[l] = nums[i]

        return len(dp)
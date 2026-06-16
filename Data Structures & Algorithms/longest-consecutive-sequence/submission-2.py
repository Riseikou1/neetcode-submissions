class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        nums.sort()
        longest = 1
        cur_streak = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] :
                continue
            elif nums[i] == nums[i-1] + 1:
                cur_streak += 1
                longest = max(longest,cur_streak)
            else :
                cur_streak = 1
        return longest
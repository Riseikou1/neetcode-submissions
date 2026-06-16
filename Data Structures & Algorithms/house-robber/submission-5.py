class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_no_rob = 0
        prev_rob = 0

        for num in nums :
            temp = prev_no_rob
            prev_no_rob = max(prev_no_rob , prev_rob)
            prev_rob = temp + num

        return max(prev_rob, prev_no_rob)
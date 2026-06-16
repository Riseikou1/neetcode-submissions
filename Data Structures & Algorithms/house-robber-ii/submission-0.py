class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 : return nums[0]

        def helper(l, r) :
            prev_rob, prev_no_rob = 0, 0
            for i in range(l, r) :
                tmp = prev_no_rob
                prev_no_rob = max(prev_no_rob, prev_rob)  # skip cur house.
                prev_rob = tmp + nums[i]  # rob cur house.
            
            return max(prev_rob, prev_no_rob)

        return max(helper(1, n), helper(0, n - 1))
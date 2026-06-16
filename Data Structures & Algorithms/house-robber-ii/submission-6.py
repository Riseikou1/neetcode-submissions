class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]

        def helper(lower, upper) :
            skip,rob = 0, 0

            for i in range(lower, upper) :
                tmp = skip
                skip = max(skip, rob + nums[i])
                rob = tmp

            return skip

        return max(helper(0,len(nums) - 1), helper(1, len(nums)))
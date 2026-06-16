class Solution:
    def rob(self, nums: List[int]) -> int:
        # if prev house was robbed, there is still 2 choices.
        # rob or skip.
        memo = {}   

        def dfs(idx, prev_rob) :
            if idx == len(nums) :
                return 0

            if (idx, prev_rob) in memo :
                return memo[(idx, prev_rob)]

            if prev_rob :
                result = dfs(idx + 1, False)

            else :
                skip = dfs(idx + 1, False)
                rob = nums[idx] + dfs(idx + 1, True)
                result = max(skip, rob)

            memo[(idx, prev_rob)] = result
            return result

        return dfs(0, False)
       
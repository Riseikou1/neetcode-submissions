class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, cur) :
            if idx == len(nums) :
                res.append(list(cur))
                return 

            dfs(idx + 1, cur + [nums[idx]])

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1] :
                idx += 1

            dfs(idx + 1, cur)

        dfs(0, [])
        return res
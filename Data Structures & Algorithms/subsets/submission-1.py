class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path) :
            if idx >= len(nums) :
                res.append(path)
                return 

            dfs(idx + 1, path)
            dfs(idx + 1, path + [nums[idx]])

        dfs(0, [])
        return res

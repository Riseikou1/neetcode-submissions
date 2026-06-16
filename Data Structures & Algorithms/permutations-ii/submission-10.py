class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(path, mask) :
            if len(path) == len(nums) :
                res.append(path) 
                return 

            for idx in range(len(nums)) :
                if mask & (1 << idx) : continue
                if idx > 0 and nums[idx] == nums[idx - 1] and mask & (1 << (idx - 1)) : continue
                dfs(path + [nums[idx]], mask | (1 << idx))

        dfs([], 0)
        return res

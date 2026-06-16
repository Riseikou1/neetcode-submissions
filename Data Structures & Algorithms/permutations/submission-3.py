class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx) :
            if idx >= len(nums) :
                res.append(nums[:])
                return 

            for i in range(idx, len(nums)) :
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        dfs(0)
        return res

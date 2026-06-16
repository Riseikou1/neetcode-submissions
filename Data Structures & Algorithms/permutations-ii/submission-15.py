class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(idx) :
            if idx >= len(nums) :
                res.append(nums[:])
                return 

            for i in range(idx, len(nums)) :
                if i > idx and nums[i] == nums[idx] : continue
                nums[i], nums[idx] = nums[idx], nums[i]

                dfs(idx + 1)
            
            for i in range(len(nums) - 1, idx, -1) :
                nums[i], nums[idx] = nums[idx], nums[i]
        
        dfs(0)
        return res
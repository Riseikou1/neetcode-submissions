class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]: 
        nums.sort()       
        def dfs(cur_sum, cur_path, idx) :
            if cur_sum == target :
                res.append(list(cur_path))
                return 
                
            if cur_sum > target or idx == len(nums) :
                return  

            for i in range(idx, len(nums)) :
                if nums[i] > target : 
                    break
                if cur_sum + nums[i] > target :
                    return 
                dfs(cur_sum + nums[i], cur_path + [nums[i]], i)

        res = []
        dfs(0, [], 0)
        return res
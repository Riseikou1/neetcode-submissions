class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(path, seen) :
            if len(path) == len(nums) :
                res.append(path)
                return 

            for i in range(len(nums)) :
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in seen : 
                    continue
                if not i in seen :
                    seen.add(i)
                    dfs(path + [nums[i]], seen)
                    seen.remove(i)
        
        dfs([], set())
        return res

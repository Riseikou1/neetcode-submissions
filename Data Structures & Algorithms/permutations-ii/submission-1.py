class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(path, visited) :
            if len(path) ==     len(nums) :
                res.append(list(path))
                return 

            for i in range(len(nums)) :
                if i in visited or (i and nums[i] == nums[i - 1] and (i - 1) not in visited) : 
                    continue
                visited.add(i)
                dfs(path + [nums[i]], visited)
                visited.remove(i)

        dfs([], set())
        return res


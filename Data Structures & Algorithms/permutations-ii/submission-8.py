class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx):
            if idx == len(nums):
                res.append(nums[:])
                return

            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])

                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]  # backtrack

        dfs(0)
        return res

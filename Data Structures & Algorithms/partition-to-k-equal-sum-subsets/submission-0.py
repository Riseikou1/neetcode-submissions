class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k : return False
        target = total // k
        nums.sort(reverse = True)
        if nums[0] > target : return False
        sides = [0] * k

        def dfs(idx) :
            if idx == len(nums) :
                return True
            for i in range(k) :
                if sides[i] + nums[idx] <= target :
                    sides[i] += nums[idx]
                    if dfs(idx + 1) : return True
                    sides[i] -= nums[idx]
                if sides[i] == 0 : break
            return False

        return dfs(0)

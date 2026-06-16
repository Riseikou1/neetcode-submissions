class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0 : return False
        nums.sort(reverse = True)
        target = total // k
        n = len(nums)

        def dfs(idx, subsetsum, k, mask) :
            if k == 0 : return True
            if subsetsum == target :
                return dfs(0, 0, k - 1, mask)
            
            for i in range(idx, n) :
                if (mask & (1 << i)) == 0 or nums[i] + subsetsum > target :
                    continue
                if dfs(i + 1, subsetsum + nums[i], k, mask ^ (1 << i)) :
                    return True

                if subsetsum == 0 :
                    return False

            return False

        return dfs(0, 0, k, (1 << n) - 1)

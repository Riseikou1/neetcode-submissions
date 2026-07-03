class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3) :
            if i and nums[i] == nums[i - 1] : continue
    
            for j in range(i + 1, n - 2) :
                if j - 1 > i and nums[j] == nums[j - 1] : continue

                for k in range(j + 1, n - 1) :
                    if k - 1 > j and nums[k] == nums[k - 1] : continue

                    for t in range(k + 1, n) :
                        if t - 1 > k and nums[t] == nums[t - 1] : continue


                        if nums[i] + nums[j] + nums[k] + nums[t] == target :
                            res.append([nums[i], nums[j], nums[k], nums[t]])
        return res

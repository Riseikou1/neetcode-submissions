class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def kSum(k, path, idx) :
            if k == 2 :
                l, r = idx, len(nums) - 1
                while l < r :
                    total = sum(path) + nums[l] + nums[r]
                    if total > target :
                        r -= 1
                    elif total < target : 
                        l += 1
                    else :
                        res.append(path + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1] :
                            l += 1
                return      
            for i in range(idx, len(nums)) :
                if i > idx and nums[i] == nums[i - 1] :
                    continue
                kSum(k - 1, path + [nums[i]] , i + 1)

        kSum(4, [], 0)
        return res

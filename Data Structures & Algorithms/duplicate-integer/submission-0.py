class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in range(len(nums)):
            if(nums[i] in counter and counter[nums[i]]>=1):
                return True
            counter[nums[i]] = counter.get(nums[i],0) + 1
        return False

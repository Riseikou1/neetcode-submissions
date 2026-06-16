class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temuujin = {}
        for i in range(len(nums)):
            temuujin[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temuujin and temuujin[complement] != i :
                return [i,temuujin[complement]]
        return []
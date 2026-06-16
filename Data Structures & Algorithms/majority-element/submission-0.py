class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        count = {}
        for num in nums :
            count[num] = count.get(num, 0) + 1
            if count[num] > target :
                return num

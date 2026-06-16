class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini, maxi = min(nums), max(nums)
        count = defaultdict(int)
        for num in nums :
            count[num] += 1

        idx = 0
        for val in range(mini, maxi + 1) :
            while count[val] > 0 :
                nums[idx] = val
                count[val] -= 1
                idx += 1
        return nums

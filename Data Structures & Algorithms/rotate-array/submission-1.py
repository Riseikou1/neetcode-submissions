class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        def helper(l, r) :
            while l < r :
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        helper(0, len(nums) - 1)
        helper(0, k - 1)
        helper(k, len(nums) - 1)

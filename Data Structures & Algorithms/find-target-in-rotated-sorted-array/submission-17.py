class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r :
            m = (l + r) // 2
            if nums[m] > nums[r] :
                l = m + 1
            else :
                r = m

        pivot = l  # idx of min el in the nums lst.
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r] :
            l = pivot
        
        else : 
            r = pivot - 1

        while l <= r :
            m = (l + r) // 2
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target :
                l = m + 1
            else :
                return m

        return -1


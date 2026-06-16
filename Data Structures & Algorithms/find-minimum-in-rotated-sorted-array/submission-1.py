class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        min_num = nums[0]

        while l <= r :

            if l == r :
                min_num = min(min_num,nums[l])
                break

            m = (l+r)//2

            if nums[m] > nums[r] :
                l = m + 1
                min_num = min(min_num,nums[m])

            else :
                r = m


        return min_num



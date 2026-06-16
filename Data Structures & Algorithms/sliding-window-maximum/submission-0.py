class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        temuujin = nums[:k]
        res = [max(temuujin)]
        for r in range(k,len(nums)):
            temuujin.append(nums[r])
            temuujin.pop(0)
            res.append(max(temuujin))

        return res

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j = 0, len(heights) - 1
        res = 0
        while i < j :
            width = j - i
            res = max(res, width * min(heights[i], heights[j]))
            if heights[i] > heights[j] :
                j -= 1
            else :
                i += 1
        return res

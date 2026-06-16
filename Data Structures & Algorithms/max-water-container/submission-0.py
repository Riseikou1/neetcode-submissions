class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i, a in enumerate(heights):
            for j in range(i+1,len(heights)):
                tmp = (j-i) * min(heights[j],a)
                res = max(res,tmp)

        return res
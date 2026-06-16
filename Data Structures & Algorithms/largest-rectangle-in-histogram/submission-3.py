class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # idx, height pair.
        res = 0

        for i, h in enumerate(heights) :
            start = i
            while stack and stack[-1][1] > h :
                idx, height = stack.pop()
                start = idx
                res = max(res, height * (i - idx))
            stack.append([start, h])

        for i, h in stack :
            res = max(res, h * (len(heights) - i))

        return res

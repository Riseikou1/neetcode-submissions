class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # idx, height pair.
        res = 0

        for idx, height in enumerate(heights) :
            start = idx
            while stack and stack[-1][1] > height :
                index, num = stack.pop()
                start = index
                res = max(res, num * (idx - index))
            stack.append([start, heights[idx]])

        for i, h in stack :
            res = max(res, (len(heights) - i) * h)
        return res

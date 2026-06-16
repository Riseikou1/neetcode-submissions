class Solution:
    def trap(self, height: List[int]) -> int:
        leftSide = [0] * len(height)
        rightSide = [0] * len(height)    
        leftSide[0] = height[0]
        rightSide[-1] = height[-1]

        for i in range(1, len(height)) :
            leftSide[i] = max(leftSide[i - 1], height[i])

        for i in range(len(height) - 2, 0, -1) :
            rightSide[i] = max(rightSide[i + 1], height[i])

        res = 0

        for i in range(len(height)) :
            tmp = min(rightSide[i], leftSide[i]) - height[i]
            res += 0 if tmp < 0 else tmp
        return res
    
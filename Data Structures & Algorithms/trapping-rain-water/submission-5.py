class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax <= rightMax :
                l += 1
                leftMax = max(leftMax,height[l])
                water = leftMax - height[l]
            else :
                r -= 1
                rightMax = max(rightMax,height[r])
                water = rightMax - height[r]

            if water > 0 :
                res += water

        return res
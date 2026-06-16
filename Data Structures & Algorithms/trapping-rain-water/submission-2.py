class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        res = 0

        leftMax = height[0]
        for i in range(1,n):
            leftMax = max(leftMax,height[i])
            left[i] = leftMax

        rightMax = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightMax = max(rightMax,height[i])
            right[i] = rightMax

        for i in range(n):
            water = min(right[i],left[i]) - height[i]
            if water > 0 :
                res += water

        return res

            



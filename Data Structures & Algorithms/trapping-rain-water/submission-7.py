class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]
        l,r = 0, len(height) - 1
        res = 0
        while l < r :
            if leftMax < rightMax : 
                if leftMax - height[l] > 0 :
                    res += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])

            else :
                if rightMax - height[r] > 0 :
                    res += rightMax - height[r]
                r -= 1  
                rightMax = max(rightMax, height[r])

        return res

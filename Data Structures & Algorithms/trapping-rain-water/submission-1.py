class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n
        res = 0

        # Fill left max
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        # Fill right max
        right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Calculate trapped water
        for i in range(n):
            water = min(left[i], right[i]) - height[i]
            if water > 0:
                res += water

        return res

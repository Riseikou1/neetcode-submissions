class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            temuujin = i
            while stack and h < stack[-1][0]:
                height,idx = stack.pop()
                max_area = max(max_area,height*(i-idx))
                temuujin = idx
            stack.append((h,temuujin))

            stack.append((h,i))

        for h,i in stack :
            area = (len(heights) - i ) * h  
            max_area = max(max_area,area)


        return max_area
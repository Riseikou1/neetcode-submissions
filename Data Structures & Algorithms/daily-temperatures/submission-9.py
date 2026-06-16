class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                tmpIdx = stack.pop()
                res[tmpIdx] += i-tmpIdx
            stack.append(i)

        return res
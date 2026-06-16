class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []

        for i in range(len(temperatures) - 1, -1, -1) :
            while stack and temperatures[stack[-1]] <= temperatures[i] :
                stack.pop()
            res.append(stack[-1] - i if stack else 0)
            stack.append(i)

        return res[::-1]

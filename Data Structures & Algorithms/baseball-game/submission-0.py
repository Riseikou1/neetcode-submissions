class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for char in operations :
            if char == "C" and stk :
                stk.pop()
            elif char == "D" and stk :
                stk.append(stk[-1] * 2)
            elif char == "+" and len(stk) >= 2 :
                first, second = stk[-1], stk[-2]
                stk.append(first + second)
            else :
                stk.append(int(char))
        
        return sum(stk)

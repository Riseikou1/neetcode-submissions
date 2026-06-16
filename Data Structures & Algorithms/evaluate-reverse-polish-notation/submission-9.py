class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for char in tokens :
            if char == "*" :
                stk.append(stk.pop() * stk.pop())
            elif char == "+" :
                stk.append(stk.pop() + stk.pop())
            elif char == "/" :
                first = stk.pop()
                second = stk.pop()
                stk.append(int(float(second) / first))
            elif char == "-" :
                first = stk.pop()
                second = stk.pop()
                stk.append(second - first)
            else :
                stk.append(int(char))

        return stk[0]

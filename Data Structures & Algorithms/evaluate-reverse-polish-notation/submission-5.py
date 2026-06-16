class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens :
            if ch == '+':
                stack.append(stack.pop()+stack.pop())
            elif ch == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif ch == '*':
                stack.append(stack.pop()*stack.pop())
            elif ch == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(float(num2) / num1))
            else :
                stack.append(int(ch))
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temuujin = list()
        for ch in tokens :
            if ch in ('+','-','*','/') :
                num2 = (temuujin.pop())
                num1 = (temuujin.pop())
                if ch == '+' :
                    ans = num2 + num1
                elif ch == '-' :
                    ans = num1 - num2
                elif ch == '*':
                    ans = num1 * num2
                elif ch == '/':
                    ans = float(num1 / num2)
                temuujin.append(int(ans))
            else :
                temuujin.append(int(ch))

        return temuujin[0]
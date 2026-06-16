class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s :
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            if ch == ']' or ch == '}' or ch == ')' :
                if len(stack) == 0 :
                    return False
                tmp = stack.pop()
                if (tmp == '(' and ch != ')') or (tmp == '{' and ch != '}') or (tmp == '[' and ch != ']'):
                    return False

        return len(stack) == 0
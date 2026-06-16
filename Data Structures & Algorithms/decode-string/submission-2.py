class Solution:
    def decodeString(self, s: str) -> str:
        times, cur_sub, stack = "", "", []

        for char in s :
            if char != "]" :
                stack.append(char)
            else :
                while stack[-1] != "[" :
                    cur_sub = stack.pop() + cur_sub
                stack.pop()
                while stack and stack[-1].isdigit() :
                    times = stack.pop() + times
                stack.append(int(times) * cur_sub)
                times, cur_sub = "", ""

        return "".join(stack)

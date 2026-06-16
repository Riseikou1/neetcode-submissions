class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for idx1, digit1 in enumerate(num1) :
            for idx2, digit2 in enumerate(num2) :
                idx = idx1 + idx2
                carry = res[idx]
                total = int(digit1) * int(digit2) + carry
                res[idx] = total % 10
                res[idx + 1] += total // 10

        while res and res[-1] == 0 : res.pop()
        return "".join(str(digit) for digit in reversed(res)) if res else "0"

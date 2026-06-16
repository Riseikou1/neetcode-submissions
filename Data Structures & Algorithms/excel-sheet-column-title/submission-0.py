class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber :
            tmp = columnNumber - 1
            digit = tmp % 26
            res.append(chr(digit + ord('A')))
            columnNumber = tmp // 26

        return "".join(reversed(res))

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
                 'C' : 100, 'D' : 500, 'M' : 1000}
        res = 0

        for idx, char in enumerate(s) :
            if idx < len(s) - 1 and roman[s[idx + 1]] > roman[char] :
                res -= int(roman[char])

            else :
                res = res + int(roman[char])

        return res

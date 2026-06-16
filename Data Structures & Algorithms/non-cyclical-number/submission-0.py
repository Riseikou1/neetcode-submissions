class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!= 1 :
            tmp = 0
            for digit in str(n) :
                tmp += int(digit) ** 2
            n = tmp
            if n in seen : return False
            seen.add(n)

        return True

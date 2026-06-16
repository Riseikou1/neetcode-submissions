class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num) :
            out = 0
            while num : 
                digit = num % 10
                out += digit ** 2
                num //= 10
            return out

        slow ,fast = n, sumOfSquares(n)
        while slow != fast :
            if fast == 1 : break
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        return fast == 1

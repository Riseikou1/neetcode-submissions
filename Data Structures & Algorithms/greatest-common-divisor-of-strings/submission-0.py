class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def gcd(a, b) :
            while b :
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1 :
            return ""

        idx = gcd(len1, len2)
        return str1[:idx]

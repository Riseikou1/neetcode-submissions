class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(ptr1, ptr2) :
            while ptr1 < ptr2 :
                if s[ptr1] != s[ptr2] :
                    return False
                ptr1 += 1
                ptr2 -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j :
            if s[i] != s[j] :
                return helper(i + 1, j) or helper(i, j - 1)
            i += 1
            j -= 1
        
        return True

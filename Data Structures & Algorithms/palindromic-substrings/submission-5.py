class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(l, r) :
            while l < r and s[l] == s[r] :
                l += 1
                r -= 1
            return l >= r
        
        memo = {len(s) : 0}
        def dfs(idx) :
            if idx in memo :
                return memo[idx]
            res = 0
            for i in range(idx, len(s)) :
                if palindrome(idx, i) :
                    res += 1

            memo[idx] = res
            return res

        return sum(dfs(i) for i in range(len(s)))

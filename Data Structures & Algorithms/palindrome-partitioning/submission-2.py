class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palindrome(l, r):
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l >= r

        def dfs(idx, path):
            if idx == len(s):
                res.append(path)
                return
            for i in range(idx, len(s)):
                if palindrome(idx, i):
                    dfs(i + 1, path + [s[idx:i + 1]])

        dfs(0, [])
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(l, r) :
            while l < r :
                if s[l] != s[r] :
                    return False
                r -= 1
                l += 1
            return True

        def dfs(idx, cur_str) :
            if idx == len(s) :
                res.append(list(cur_str))

            for i in range(idx, len(s)) :
                if isPalindrome(idx, i) :
                    cur_str.append(s[idx : i + 1])
                    dfs(i + 1, cur_str)
                    cur_str.pop()
        
        dfs(0, [])
        return res


       
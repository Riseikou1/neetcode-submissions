class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(word) :
            l, r = 0, len(word) - 1
            while l < r :
                if word[l] != word[r] :
                    return False
                l += 1
                r -= 1
            return True

        def dfs(idx, cur_str) :
            if idx == len(s) :
                res.append(list(cur_str))

            for i in range(idx, len(s)) :
                part = s[idx : i + 1]

                cur_str.append(part)

                if isPalindrome(part) :
                    dfs(i + 1, cur_str)
                
                cur_str.pop()
        
        dfs(0, [])
        return res


       
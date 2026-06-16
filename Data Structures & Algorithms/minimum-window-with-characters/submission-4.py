class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) : return ""
        
        book = {}
        for ch in t :
            book[ch] = book.get(ch,0) + 1

        l = 0
        reslen = float('inf')
        res = [-1,-1]
        window = {}
        have,need = 0,len(book)

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1
            if ch in book and window[ch] == book[ch]:
                have += 1

            while have == need :
                if (r-l+1) < reslen :
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in book and window[s[l]] < book[s[l]] :
                    have -=1 
                l += 1

        l,r = res
        return s[l:r+1] if reslen!=float('inf') else ""
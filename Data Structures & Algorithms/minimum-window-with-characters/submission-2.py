class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s) :
            return ""

        countT,window ={}, {}

        for c in t :
            countT[c] = countT.get(c,0)+1

        have , need = 0, len(countT)
        res,reslen = [-1,-1],float('inf')
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1

            if ch in countT and countT[ch] == window[ch] :
                have += 1
            
            while have == need :

                if (r-l+1) < reslen:
                    reslen = r-l + 1
                    res = [l,r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1] if reslen != float('inf') else "" 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        temuujin = {}
        for ch in s :
            temuujin[ch] = temuujin.get(ch,0) +1 

        for ch in t :
            if ch not in temuujin :
                return False
            if temuujin[ch] == 0 :
                return False
            temuujin[ch] -= 1

        return True
        
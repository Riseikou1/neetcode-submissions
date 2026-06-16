class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        temuujin1 = {}
        temuujin2 = {}

        for i in range(len(s)):
            temuujin1[s[i]] = temuujin1.get(s[i],0) + 1
            temuujin2[t[i]] = temuujin2.get(t[i],0) + 1
        
        return temuujin1 == temuujin2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        map1 = {}
        map2 = {}
        l = 0

        for ch in s1 :
            map1[ch]  = map1.get(ch,0) + 1

        for r in range(len(s2)):

            map2[s2[r]] = map2.get(s2[r],0) + 1

            if r - l + 1 > len(s1):
                map2[s2[l]] -= 1
                if map2[s2[l]] == 0:
                    del map2[s2[l]]
                l += 1

            if map1 == map2 :
                return True

        return False

            
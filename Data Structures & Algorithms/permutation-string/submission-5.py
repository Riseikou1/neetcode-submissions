class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False

        map_1, map_2 = {}, {}
        for i in range(len(s1)) :
            map_1[s1[i]] = map_1.get(s1[i], 0) + 1
            map_2[s2[i]] = map_2.get(s2[i], 0) + 1
        if map_1 == map_2 : return True

        l = 0
        for r in range(len(s1), len(s2)) :
            map_2[s2[l]] -= 1
            if not map_2[s2[l]] :
                del map_2[s2[l]]
            l += 1
            map_2[s2[r]] = map_2.get(s2[r], 0) + 1
            if map_1 == map_2 : return True

        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        s1_count, s2_count = [0] * 26, [0] * 26
        l = 0

        for i in range(len(s1)) :
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        have = sum(1 for i in range(26) if s1_count[i] == s2_count[i])
        if have == 26 : return True

        for i in range(len(s1), len(s2)) :
            idx = ord(s2[i]) - ord('a')
            # add the r idx and count.
            s2_count[idx] += 1
            if s2_count[idx] - 1 == s1_count[idx] :
                have -= 1
            elif s2_count[idx] == s1_count[idx] :
                have += 1

            # delete l char and count.
            idx = ord(s2[l]) - ord('a')
            s2_count[idx] -= 1
            if s2_count[idx] + 1 == s1_count[idx] :
                have -= 1
            elif s2_count[idx] == s1_count[idx] :
                have += 1
            l += 1

            if have == 26 :
                return True

        return False

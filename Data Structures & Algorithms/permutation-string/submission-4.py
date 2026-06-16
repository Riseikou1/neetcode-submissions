class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False

        count1 = [0]*26
        count2 = [0]*26
        l = 0
        matches = 26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1

        matches = sum(1 if count1[i] == count2[i] else 0 for i in range(26))

        if matches == 26 :
            return True

        for r in range(len(s1),len(s2)):
            ch = ord(s2[r]) - ord('a')
            count2[ch] += 1

            if count2[ch] == count1[ch] :
                matches += 1
            elif count2[ch] -1 == count1[ch]:
                matches -= 1

            

            if (r-l+1) > len(s1):
                left_char = ord(s2[l]) - ord('a')
                count2[left_char] -= 1
                if count2[left_char] == count1[left_char] :
                    matches += 1
                elif count2[left_char] +1 == count1[left_char]:
                    matches -= 1
                l += 1

            if matches == 26 :  
                return True

        return False


        
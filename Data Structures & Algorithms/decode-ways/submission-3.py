class Solution:
    def numDecodings(self, s: str) -> int:
        curr, two_ahead = 0, 0
        one_ahead = 1

        for i in range(len(s) -1, -1, -1) :
            if s[i] == "0" : 
                curr = 0

            else :
                curr += one_ahead

            if i + 1 < len(s) and s[i] != "0" and int(s[i : i + 2]) <= 26 :
                curr += two_ahead

            one_ahead, two_ahead, curr = curr, one_ahead, 0

        return one_ahead
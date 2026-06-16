class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [0] * 26
        for char in s :
            count[ord(char) - ord('a')] += 1

        max_freq = max(count)
        if max_freq > (len(s) + 1) // 2 : return ""
        res = [""] * len(s)
        max_indx = count.index(max_freq)
        idx = 0
        max_char = chr(max_indx + ord('a')) 

        while count[max_indx] :
            res[idx] = max_char
            idx += 2
            count[max_indx] -= 1

        for i in range(25, -1, -1) :
            while count[i] : 
                if idx >= len(s) :
                    idx = 1
                count[i] -= 1 
                res[idx] = (chr(i + ord('a')))
                idx += 2

        return "".join(res)

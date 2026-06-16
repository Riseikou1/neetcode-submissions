class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32) :
            if (n >> i) & 1 :
                binary = "1" + binary
            else :
                binary = "0" + binary

        res = 0
        for idx, char in enumerate(binary) :
            if char == "1" :
                res |= (1 << idx)

        return res

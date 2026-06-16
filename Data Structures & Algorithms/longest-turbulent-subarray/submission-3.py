class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1 : return 1
        res, l, prev = 0, 0, ""
        r = 1
        while r < len(arr) :
            if arr[r] > arr[r - 1] and prev != ">" :
                r += 1
                prev = ">"
            
            elif arr[r] < arr[r - 1] and prev != "<" :
                r += 1
                prev = "<"

            else :
                prev = ""
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1

            res = max(res, r - l)

        return res

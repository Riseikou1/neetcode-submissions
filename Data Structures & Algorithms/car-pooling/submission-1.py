class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l, r = float('inf'), float('-inf')
        for pas, start, end in trips :
            l = min(l, start)
            r = max(r, end)

        n = r - l + 1
        paschange = [0] * (n + 1)
        for pas, start, end in trips :
            paschange[start - l] += pas
            paschange[end - l] -= pas

        curval = 0
        for change in paschange :
            curval += change
            if curval > capacity :
                return False

        return True


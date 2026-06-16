class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        memo = {}
        length = mountainArr.length()
        def get(m) :
            if not m in memo :
                memo[m] = mountainArr.get(m)
            return memo[m]

        l, r = 1, length - 2
        while l <= r :
            m = l + (r - l) // 2
            left = get(m - 1)
            mid = get(m)
            right = get(m + 1)
            if left < mid < right :
                l = m + 1
            elif left > mid > right :
                r = m - 1
            else :
                break
        peak = m

        def binary_search(l, r, ascending) :
            while l <= r :
                m = l + (r - l) // 2 
                val = get(m)
                if val == target :
                    return m
                elif ascending == (val < target) :
                    l = m + 1
                else :
                    r = m - 1

            return -1

        res = binary_search(0, peak, True)
        if res != -1 :
            return res

        return binary_search(peak, length - 1, False)

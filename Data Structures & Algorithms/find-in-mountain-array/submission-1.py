class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2

        # 1st iteration : search for the peak idx.
        while l < r :
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            val_after = mountainArr.get(m + 1)
            val_before = mountainArr.get(m - 1)
            if val_before < val > val_after :    
                l = m
                break
            elif val < val_after :
                l = m + 1
            else :
                r = m - 1

        peak = l
        res = float("inf")  # idx of target
        # 2nd and 3rd --> search for the left and at the right side.

        l, r = 0, peak
        while l <= r :   # on the increasing portion.
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val == target :
                res = m
                break
            elif val > target :
                r = m - 1
            else :
                l = m + 1
        
        l, r = peak + 1, length - 1
        while l <= r :
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val == target :
                res = min(res, m)
                break
            elif val > target :
                l = m + 1
            else :
                r = m - 1

        return -1 if res == float("inf") else res

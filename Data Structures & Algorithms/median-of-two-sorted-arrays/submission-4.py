class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(a) + len(b)
        half = (total + 1) // 2
        l, r = 0, len(a)

        while l <= r :
            x = m = l + (r - l) // 2
            y = half - x
            aleft = a[x - 1] if (x - 1) >= 0 else float("-inf")
            aright = a[x] if x < len(a) else float("inf")
            bleft = b[y - 1] if (y - 1) >= 0 else float("-inf")
            bright = b[y] if y < len(b) else float("inf")

            if min(aright, bright) >= max(aleft, bleft) :
                if total & 1 :
                    return max(aleft, bleft)
                else :
                    return (max(aleft, bleft) + min(aright, bright)) / 2

            elif aleft > bright :
                r = m - 1

            else :
                l = m + 1


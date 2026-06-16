class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2) + 1) //2
        A,B = (nums1,nums2) if len(nums1) <= len(nums2) else (nums2,nums1)
        l,r = 0,len(A)

        while l <= r :
            x = l + (r-l)//2
            y = half - x
            
            Aleft = A[x - 1] if x > 0 else float('-inf')
            Aright = A[x] if x < len(A) else float('inf')
            Bleft = B[y - 1] if y > 0 else float('-inf')
            Bright = B[y] if y < len(B) else float('inf')

            if max(Aleft,Bleft) <= min(Aright,Bright):
                if (len(nums1) + len(nums2))%2 ==0 :
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else :
                    return max(Aleft,Bleft)

            elif Aleft > Bright:
                r = x - 1
            else :
                l = x + 1
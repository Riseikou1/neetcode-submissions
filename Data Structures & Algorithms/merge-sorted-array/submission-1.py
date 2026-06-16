class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while nums2:
            cur = nums2.pop()
            l, r = 0, m  
            while l < r:
                mid = l + (r - l) // 2
                if nums1[mid] < cur:
                    l = mid + 1
                else:
                    r = mid
            idx = l

            for i in range(m, idx, -1):
                nums1[i] = nums1[i - 1]

            nums1[idx] = cur
            m += 1  

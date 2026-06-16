class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = []
        i, j = 0, 0

        for idx in range(len(nums1) + len(nums2)) :
            if i < len(nums1) and j >= len(nums2) :
                tmp.append(nums1[i])
                i += 1
            elif i >= len(nums1) and j < len(nums2) :
                tmp.append(nums2[j])
                j += 1
            elif nums2[j] >= nums1[i] :
                tmp.append(nums1[i])
                i += 1
            else :
                tmp.append(nums2[j])
                j += 1

        if len(tmp) & 1 :
            return tmp[len(tmp) // 2]
        
        return (tmp[len(tmp) // 2] + tmp[len(tmp) // 2 - 1]) / 2

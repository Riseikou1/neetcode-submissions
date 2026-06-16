class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = list()
        i = j = 0
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else :
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        return (merged[(len(merged)-1)//2] + merged[len(merged)//2])/2
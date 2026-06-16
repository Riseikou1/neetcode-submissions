class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, mid, right) :
            tmp = arr.copy()
            l, k, r = left, left, mid + 1

            while l <= mid and r <= right :
                if tmp[l] <= tmp[r] :
                    arr[k] = tmp[l]
                    l += 1
                else :
                    arr[k] = tmp[r]
                    r += 1
                k += 1
            while l <= mid :
                arr[k] = tmp[l]
                l += 1
                k += 1
            while r <= right :
                arr[k] = tmp[r]
                k += 1
                r += 1

        def mergeSort(arr, left, right) :
            if left >= right : return 
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)

        mergeSort(nums, 0, len(nums) - 1)
        return nums

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def helper(arr_total) :
            part = 1
            total = 0
            for num in nums :
                if total + num > arr_total :
                    part += 1
                    if part > k : return False
                    total = 0
                total += num

            return part <= k

        while l < r :
            m = (r + l) // 2

            if helper(m) :
                r = m

            else :
                l = m + 1

        return l
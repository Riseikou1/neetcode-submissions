class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1] * 2 for _ in range(n)]
        res = 1

        for i in range(n - 2, -1, -1) :
            if arr[i] > arr[i + 1] :
                dp[i][1] = dp[i + 1][0] + 1
            elif arr[i] < arr[i + 1] :
                dp[i][0] = dp[i + 1][1] + 1
            
            res = max(res, dp[i][0], dp[i][1])

        return res

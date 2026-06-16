class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        memo = {}
        def dfs(idx, sign) :
            if idx == len(arr) :
                return 1

            if (idx, sign) in memo :
                return memo[(idx, sign)]

            res = 1
            if ((sign and arr[idx] > arr[idx - 1]) or (not sign and arr[idx] < arr[idx - 1])) :
                res = 1 + dfs(idx + 1, not sign)

            memo[(idx, sign)] = res
            return res
        
        max_shit = 1
        for i in range(1, len(arr)) :
            max_shit = max(max_shit, dfs(i, True), dfs(i, False))
            
        return max_shit

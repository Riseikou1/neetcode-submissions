class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum + 1) // 2
        memo = {}

        def dfs(idx, total) :
            if idx >= len(stones) or total >= target : 
                return abs(total - (stoneSum - total))

            if (idx, total) in memo : return memo[(idx, total)]

            res = min(dfs(idx + 1, total), dfs(idx + 1, total + stones[idx]))
            memo[(idx, total)] = res
            return res

        return dfs(0, 0)


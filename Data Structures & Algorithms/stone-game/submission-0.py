class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(l, r) :
            if l > r : return 0
            if (l, r) in memo : 
                return memo[(l, r)]

            even = True if (r-l) % 2 else False
            right = piles[r] if even else 0
            left = piles[l] if even else 0
            res = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            memo[(l, r)] = res
            return res

        return dfs(0, len(piles) - 1) > sum(piles) // 2
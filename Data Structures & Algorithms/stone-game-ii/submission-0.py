class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def dfs(alice_turn, idx, m) :
            if idx >= len(piles) : return 0
            if (alice_turn, idx, m) in memo :
                return memo[(alice_turn, idx, m)]

            res = 0 if alice_turn else float('inf')
            total = 0
            for x in range(1, 2 * m + 1) :
                if idx + x > len(piles) : break
                total += piles[idx + x - 1]

                if alice_turn :
                    res = max(res, total + dfs(not alice_turn, idx + x, max(m, x)))
                
                else :
                    res = min(res, dfs(not alice_turn, idx + x, max(m, x)))

            memo[(alice_turn, idx, m)] = res
            return res

        return dfs(True, 0, 1)


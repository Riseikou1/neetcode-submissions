class Solution:
    def makesquare(self, temuujin: List[int]) -> bool:
        n = len(temuujin)
        total = sum(temuujin) 
        if total % 4 : return False
        target = total // 4
        temuujin.sort(reverse = True)
        if temuujin[0] > target : return False
        dp = [float('-inf')] * (1 << n) # all possible subsets (expressed by bit mask)

        def dfs(mask) :
            if mask == 0 : return 0
            if dp[mask] != float('-inf') :
                return dp[mask]
            
            for i in range(n) :
                if mask & (1 << i) :
                    res = dfs(mask ^ (1 << i))
                    if res >= 0 and res + temuujin[i] <= target :
                        dp[mask] = (res + temuujin[i]) % target
                        return dp[mask]

            dp[mask] = -1
            return -1

        return not dfs((1 << n)- 1)

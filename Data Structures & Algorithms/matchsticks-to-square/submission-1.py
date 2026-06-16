class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)
        total = sum(matchsticks)
        if total % 4 : return False
        target = total // 4
        if matchsticks[0] > target : return False
        sides = [0] * 4

        def dfs(idx) :
            if idx == len(matchsticks) :
                return True
            for i in range(4) :
                if sides[i] + matchsticks[idx] <= target :
                    sides[i] += matchsticks[idx]
                    if dfs(idx + 1) : return True
                    sides[i] -= matchsticks[idx]
                if sides[i] == 0 : 
                    break
            return False

        return dfs(0)

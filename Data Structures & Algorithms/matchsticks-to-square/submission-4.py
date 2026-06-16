class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 : return False
        target = total // 4
        sides = [target] * 4
        matchsticks.sort(reverse = True)
        if matchsticks[0] > target :
            return False

        def dfs(idx) :
            if idx >= len(matchsticks) :
                return sum(sides) == 0
            
            for i in range(4) :
                if sides[i] - matchsticks[idx] >= 0 :
                    sides[i] -= matchsticks[idx]
                    if dfs(idx + 1) :
                        return True
                    sides[i] += matchsticks[idx]
                    
                if sides[i] == target :
                    break

            return False

        return dfs(0)

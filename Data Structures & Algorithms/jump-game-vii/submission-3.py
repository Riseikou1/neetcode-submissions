class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q :
            cur = q.popleft()
            if cur == len(s) - 1 : 
                return True
                
            start = max(cur + minJump, farthest + 1)
            end = min(cur + maxJump, len(s) - 1)

            for i in range(start, end + 1) :
                if s[i] == '0' :
                    q.append(i)
            farthest = end

        return False

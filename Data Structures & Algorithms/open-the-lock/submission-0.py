class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited : return -1
        turns = 0
        visited.add('0000')

        def helper(cur) :
            res = []
            for i in range(4) :
                for move in [1, -1] :
                    changed = str((int(cur[i]) + move) % 10)
                    nxt_str = list(cur)
                    nxt_str[i] = changed
                    res.append("".join(nxt_str))
            return res

        q = deque(["0000"])
        while q :
            for _ in range(len(q)) :
                cur_str = q.popleft()
                if cur_str == target : return turns
                for nxt in helper(list(cur_str)) :
                    if nxt not in visited :
                        visited.add(nxt)
                        q.append(nxt)    
            turns += 1 
        return -1

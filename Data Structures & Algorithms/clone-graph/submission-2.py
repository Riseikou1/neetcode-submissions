"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        temuujin = defaultdict(lambda : Node())
        if not node : return None
        temuujin[node].val = node.val
        q = deque([node])

        while q :
            cur = q.popleft()
            for nei in cur.neighbors :
                if nei not in temuujin :
                    temuujin[nei].val = nei.val
                    q.append(nei)
                temuujin[cur].neighbors.append(temuujin[nei])
        
        return temuujin[node]
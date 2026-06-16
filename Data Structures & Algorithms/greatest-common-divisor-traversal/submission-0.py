class UnionFind :
    def __init__(self, n) :
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, x) :
        if x != self.parent[x] :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) :
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y : return
        self.count -= 1 
        if self.rank[root_x] < self.rank[root_y] :
            root_x, root_y = root_y, root_x
        self.rank[root_x] += self.rank[root_y]
        self.parent[root_y] = root_x

    def isConnected(self) :
        return self.count == 1

def prime_factor(num) :
    factors = set()
    while num % 2 == 0 :
        factors.add(2)
        num //= 2
    f = 3
    while f * f <= num :
        while num % f == 0 :
            factors.add(f)
            num //= f
        f += 2
    if num > 1 :
        factors.add(num)
    return factors

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n == 1 : return True
        if 1 in nums : return False
        uf = UnionFind(n)
        factor_idx = {}

        for idx, num in enumerate(nums) :
            for f in prime_factor(num) :
                if f in factor_idx :
                    uf.union(idx, factor_idx[f])
                else :
                    factor_idx[f] = idx

        return uf.isConnected()

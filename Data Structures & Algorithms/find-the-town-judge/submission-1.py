class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for src, dst in trust :
            delta[src] -= 1
            delta[dst] += 1
        
        for key, count in delta.items() :
            if count == n - 1 : return key

        return -1
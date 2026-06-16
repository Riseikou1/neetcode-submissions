class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        memo = {}
        
        for start, end in intervals :
            for num in range(start, end + 1) :
                length = end - start + 1
                memo[num] = length if num not in memo else min(memo[num], length)

        res = []
        for q in queries :
            res.append(memo[q] if q in memo else -1)

        return res

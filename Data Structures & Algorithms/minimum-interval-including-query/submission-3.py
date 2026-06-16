class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        res = []

        for start, end in intervals :
            for i in range(start, end + 1) :
                if i not in hashMap :
                    hashMap[i] = end - start + 1
                else :
                    hashMap[i] = min(hashMap[i], end - start + 1)

        for q in queries :
            res.append(hashMap[q] if q in hashMap else -1)

        return res
                    
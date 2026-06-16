class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashMap = defaultdict(int)

        for num1, num2 in intervals :
            dist = num2 - num1 + 1
            for i in range(num1, num2 + 1) :
                if i not in hashMap :
                    hashMap[i] = dist
                else :
                    hashMap[i] = min(hashMap[i], dist)

        res = []
        for num in queries :
            if num not in hashMap :
                res.append(-1)
            else :
                res.append(hashMap[num])

        return res
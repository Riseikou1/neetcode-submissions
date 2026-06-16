class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums :
            temuujin[num] = temuujin.get(num,0)+1

        for key, val in temuujin.items() :
            freq[val].append(key)

        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k :
                    return res

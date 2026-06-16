class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        for num in nums :
            temuujin[num] = temuujin.get(num,0) + 1


        new_shit = []

        for  _ in range(k):
            max_freq = -1
            max_key = None
            for key in temuujin :
                if temuujin[key] > max_freq :
                    max_key = key
                    max_freq = temuujin[key]  
            new_shit.append(max_key)
            del temuujin[max_key]
        return new_shit      
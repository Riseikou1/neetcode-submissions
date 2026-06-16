class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temuujin = {}
        heap = [[] for _ in range(len(nums)+1)]

        for num in nums :
            temuujin[num] = temuujin.get(num,0) + 1

        for key, value in temuujin.items():
            heap[value].append(key)

        output = []

        for i in range(len(nums),0,-1):
            for j in heap[i]:
                if len(output) == k :
                    return output
                output.append(j)

        return output


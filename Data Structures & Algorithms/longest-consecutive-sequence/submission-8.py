class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        temuujin = defaultdict(int)
        nums.sort()
        res = 0

        for num in nums :
            if not temuujin[num]:
                temuujin[num] = temuujin[num-1] + temuujin[num+1] + 1
                temuujin[num-temuujin[num-1]] = temuujin[num]
                temuujin[num+temuujin[num+1]] = temuujin[num]

                res = max(res,temuujin[num])

        return res
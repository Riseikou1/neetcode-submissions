class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temuujin = defaultdict(int)
        temuujin[0] = 1
        res = 0
        prefix = 0
        for num in nums :
            prefix += num
            res += temuujin[prefix - k]
            temuujin[prefix] = temuujin.get(prefix, 0) + 1

        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        hash_map = {}
        nums.sort()
        if not nums : return 0

        for num in nums :
            if num - 1 in hash_map :
                hash_map[num] = hash_map[num - 1] + 1

            else :
                hash_map[num] = 1
        
        return max(hash_map.values())

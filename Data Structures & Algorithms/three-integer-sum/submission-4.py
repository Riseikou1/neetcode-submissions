class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temuujin = defaultdict(int)
        nums.sort()
        res = []
        for num in nums :
            temuujin[num] = temuujin.get(num,0) + 1

        for i in range(len(nums)):
            temuujin[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                temuujin[nums[j]] -= 1

                if j-1 > i and nums[j] == nums[j-1]:
                    continue

                target = - (nums[i] + nums[j])

                if temuujin[target] > 0:
                    res.append([nums[i],nums[j],target])

            for j in range(i+1,len(nums)):
                temuujin[nums[j]] += 1

        return res
                    

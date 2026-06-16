class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temuujin = {}

        for i in range(len(numbers)) :
            complement = target - numbers[i]
            if complement in temuujin and temuujin[complement]!=i:
                return [temuujin[complement]+1,i+1]
            temuujin[numbers[i]] = i

        return []
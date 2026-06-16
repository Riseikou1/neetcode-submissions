class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1,max(piles)

        while l < r:
            m = l +(r-l)//2

            total = 0
            for num in piles :
                total += math.ceil(num/m)

            if total > h :
                l = m + 1
            else :
                r = m
        
        return l
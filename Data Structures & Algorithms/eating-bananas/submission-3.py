class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r :
            m = (r + l) // 2
            total = sum((p + m - 1)//m for p in piles)
            
            if total > h :
                l = m + 1
            else :
                r = m

        return l
            

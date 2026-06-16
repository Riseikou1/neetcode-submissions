class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        temuujin = list(count.keys())
        heapq.heapify(temuujin)

        while temuujin :
            first = temuujin[0] 
            for i in range(first, first + groupSize) :
                if not count[i] : return False
                count[i] -= 1
                if count[i] == 0 :
                    if i != temuujin[0] : return False
                    heapq.heappop(temuujin)
        return True

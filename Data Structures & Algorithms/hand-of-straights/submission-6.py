class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()

        for num in hand :
            start = num
            while count[start] : 
                start -= 1
            while start <= num :
                while count[start] :
                    for i in range(start, start + groupSize) :
                        if not count[i] : return False
                        count[i] -= 1
                start += 1

        return True

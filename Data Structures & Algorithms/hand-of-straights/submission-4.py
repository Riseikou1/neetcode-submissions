class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for i in sorted(count) :
            if count[i] > 0 :
                all_occurances = count[i]
                for j in range(groupSize) :
                    count[i + j] -= all_occurances
                    if count[i + j] < 0 :
                        return False

        return True

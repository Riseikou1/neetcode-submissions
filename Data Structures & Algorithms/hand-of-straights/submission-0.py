class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        minval = min(hand)
        min_heap = []
        if n % groupSize : return False
        count = defaultdict(int)

        for num in hand :
            heapq.heappush(min_heap, num)
            count[num] += 1

        cur = 0
        while min_heap :
            if minval not in count :
                return False

            count[minval] -= 1
            if count[minval] == 0 :
                del count[minval]
                heapq.heappop(min_heap)
            minval += 1

            cur += 1
            if cur == groupSize :
                cur = 0
                while min_heap and min_heap[0] not in count :
                    heapq.heappop(min_heap)

                if min_heap :
                    minval = min_heap[0]

        return True


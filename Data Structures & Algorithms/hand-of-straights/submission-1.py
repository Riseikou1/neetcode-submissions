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

        while min_heap :
            while min_heap and min_heap[0] not in count :
                heapq.heappop(min_heap)

            if not min_heap : break
            minval = min_heap[0]

            for i in range(groupSize) :
                cur = minval + i
                if cur not in count :
                    return False
                count[cur] -= 1
                if count[cur] == 0 :
                    del count[cur]

        return True


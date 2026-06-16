class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize : return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap :
            first = min_heap[0]
            for num in range(first, first + groupSize) :
                if not num in count : return False
                count[num] -= 1
                if count[num] == 0 :
                    if num != min_heap[0] : return False
                    del count[num]
                    heapq.heappop(min_heap)

        return True
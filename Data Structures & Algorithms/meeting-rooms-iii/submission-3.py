class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        min_heap = []
        avail_rooms = [i for i in range(n)]
        count = [0] * n

        for start, end in meetings :
            while min_heap and min_heap[0][0] <= start :
                _, room_num = heapq.heappop(min_heap)
                heapq.heappush(avail_rooms, room_num)

            if not avail_rooms :
                end_time, room_num = heapq.heappop(min_heap)
                end = end_time + (end - start)
                heapq.heappush(avail_rooms, room_num)

            room_num = heapq.heappop(avail_rooms)
            heapq.heappush(min_heap, [end, room_num])
            count[room_num] += 1

        return count.index(max(count))

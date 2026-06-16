class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [(0, i) for i in range(n)]   # (end_time, room_num)
        count = [0] * n

        for start, end in meetings :
            while available and available[0][0] < start :
                _, room_num = heapq.heappop(available)
                heapq.heappush(available, (start, room_num))

            end_time, room = heapq.heappop(available)
            heapq.heappush(available, (end_time + (end - start), room))
            count[room] += 1

        return count.index(max(count))

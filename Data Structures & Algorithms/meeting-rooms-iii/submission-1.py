class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)] # stores available room nums.
        used = []  # stores (ending_time, room_number)
        count = [0] * n

        for start, end in meetings :
            while used and used[0][0] <= start :
                _, room_num = heapq.heappop(used)
                heapq.heappush(available, room_num)
            
            if not available :
                end_time, room_number = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room_number)
            
            room_number = heapq.heappop(available)
            heapq.heappush(used, (end, room_number))
            count[room_number] += 1

        return count.index(max(count))

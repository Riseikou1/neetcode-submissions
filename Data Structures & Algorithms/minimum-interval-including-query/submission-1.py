class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0

        for val in sorted(queries) :
            while i < len(intervals) and val >= intervals[i][0] :
                dist = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (dist, intervals[i][1]))
                i += 1

            while min_heap and min_heap[0][1] < val :
                heapq.heappop(min_heap)

            res[val] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]

